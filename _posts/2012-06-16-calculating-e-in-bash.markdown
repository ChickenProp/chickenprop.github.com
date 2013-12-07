---
layout: post
title: Calculating e in bash
draft: true
---
*(Fri, 6 Dec 2013: Importing this post from its [original home as a gist](https://gist.github.com/ChickenProp/2942612).)*

The point of this post is an attempt to calculate e to given precision in bash, a challenge given in a job listing that I saw recently. I kind of got [nerd sniped](http://xkcd.com/356/). I wrote this as I went along, so there may be inconsistencies.

###First attempt###

The obvious method to compute e is as the infinite sum of 1/n!, n from 0 to ∞. This converges quickly, but how far do we have to calculate to get the n'th digit of e? We can deal with that later.

We obviously need a factorial function.

    fac() {
        if [[ $1 -eq 0 ]]; then
            echo 1
        else
            echo $(( $1 * `fac $(($1 - 1))` ))
        fi
    }

Since we only have integer division, we obviously can't calculate 1/2!. But note that x/a! + y/(a+1)! = (x(a+1) + y)/(a+1)!. We can use this to recursively calculate (sum 1/k! \[0 ≤ k ≤ n\]) as numer(n)/n!, where numer(0) = 0, numer(k) = k\*numer(k-1) + 1.

    numer() {
        if [[ $1 -eq 0 ]]; then
            echo 1
        else
            echo $(( $1 * `numer $(($1 - 1))` + 1 ))
        fi
    }

So now we can calculate the partial sums. Since we still only have integer division, we need to multiply them by a power of 10 to get rid of the decimal point.

    nthsum() {
        echo $(( 10**($1-1) * `numer $1` / `fac $1` ))
    }

Note that this fails for n=0 (10\*\*-1 isn't allowed), but we can live with that.

So this kind of works:

    $ for i in `seq 1 15`; do nthsum $i; done
    2
    25
    266
    2708
    27166
    271805
    2718253
    27182787
    271828152
    2718281801
    27182818261
    2252447557
    -1174490000
    104582974
    1946803

Up to n=11, we accurately calculate the first (n-3) digits of e. For n=12 and above, we get integer overflows.

It doesn't look like we can go very far with this: the numbers we're working with are simply too large.

###Second attempt###

If you google "algorithm to calculate a specific digit of e", this paper comes up: <http://eprints.utas.edu.au/121/1/Calculation_of_e.pdf>. It provides a simple algorithm using (mostly) integer arithmetic, implemented in ALGOL. It's simple enough to translate into bash:

    ecalc() {
        let n=$1
        echo -n 2.
    
        for (( j = n; j >= 2; j-- )); do
            coef[j]=1
        done
    
        for (( i = 1; i <= n; i++ )); do
            let carry=0
            for (( j = n; j >= 2; j-- )); do
                let temp=coef[j]*10+carry
                let carry=temp/j
                let coef[j]=temp-carry*j
            done
            echo -n $carry
        done
        echo
    }

This isn't quite accurate: the original algorithm calculates m such that m! > 10^(n+1), and the loops over j go from m to 2 instead of n to 2. This means the algorithm is inaccurate for small n. (For n ≥ 27, n! > 10^(n+1) so it works out okay; for 22 ≤ n ≤ 26, we have 10^(n-1) < n! < 10^(n+1) and the result is accurate anyway. It seems like the algorithm is unnecessarily conservative, but we might also find that m! > 10^(n-1) is insufficient for larger n.) For large n, we do unnecessary work, but get the correct result.

We can fix both these problems, but this algorithm isn't especially nice anyway. Its time complexity is O(n^2). Can we do better?

###Third attempt###

(Spoiler alert: this doesn't go so well.)

The same google search also gives this page: <http://www.hulver.com/scoop/story/2004/7/22/153549/352> which hints at an algorithm without providing it explicitly. We can adapt our first attempt for this.

Write numer(n) as a\_n, so a\_0 = 1 and a\_n = n * a\_(n-1) + 1. This gives 1/0! + 1/1! + ... + 1/n! = a\_n / n!. We know that e = lim [n→∞] a\_n / n!; but more than this, we can show that for any n ≥ 1, a\_n / n! < e < (a\_n + 1)/n!.

(Proof of this: (a\_n+1) / n! = 1/0! + 1/1! + ... + 1/n! + 1/n!. This is greater than e if 1/n! > 1/(n+1)! + 1/(n+2)! + ..., which holds if 1 > 1/(n+1) (1 + 1/(n+2) (1 + ... )). For n ≥ 1, RHS is ≤ 1/2 (1 + 1/3 (1 + ... )) which we know is e-2 < 1.)

So if a\_n / n! and (a\_n + 1) / n! agree up to k decimal places, these must be the first k decimal places of e.

Moreover, we can extract specific decmial places while keeping to integer division: the fractional part of x/y is (x%y)/y, so the first decmal digit is int( (10\*(x%y))/y ) or int( (x%y)/(y/10) ) (assuming y%10 = 0), and we can extract further digits by doing the same thing again.

This gives us an algorithm for calculating e to n decimal places, one digit at a time:

    ecalc() {
        let a=1
        let b=1
        let d=0
        let k=1
        let n=$1
    
        while (( d <= n )); do
            while (( a/b != (a+1)/b || b%10 != 0 )); do
                let a=k*a+1
                let b*=k
                let k+=1
            done
    
            echo -n $(( a / b ))
            let d+=1
            let a%=b
            let b/=10
        done
    
        echo
    }

Unfortunately, this only works up to three decimal places before we get overflows. The problem is that b only gets a new power of 10 every time k%5 = 0. Unfortunately 24!/10000 overflows, so we only get digits from k=5, 10, 15, 20. (In fact, `ecalc 4` is also correct; but this seems to be just coincidence.)

We can delay the inevitable by keeping track of powers of ten explicitly: when we generate a new digit, if b%10 != 0, increment a counter and consider (10^powten \* a)/b and (10^powten \* (a+1))/b. This gives us a few more digits, but before long 10^powten \* a overflows.

So, how to get around this? Why not just implement arbitrary-precision integers in bash?

It sounds crazy, but we don't actually need a complete implementation. The only operations we need are:

- Add one to a bigint.
- Multiply a bigint by an int.
- Divide a bigint by 10.
- Modulo a bigint by 10.
- Integer division of bigints, with small ratio.
- Modulo a bigint by another bigint, also with small ratio.

The latter two can be implemented with subtraction and comparison, so it shouldn't be too hard.

Let's represent a big integer as an array of numbers, each smaller than 2^32. Since bash can represent numbers up to 2^63 - 1, we can raise n up to 2^31 - 1 before overflows become a serious problem. As of 2010, e was only known up to about 2^40 digits, so this is an acceptable limit. But it's admittedly quite arbitrary, and there's no reason to hardcode it.
