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

    let MAXINT=2**32

We'll want some way of taking an array of numbers and turning it into a bigint, if some of its elements are greater than MAXINT or less than 0. I don't think there's a convenient way of passing around arrays in bash, so let's use a register-based approach, and operate destructively on the variable $res. (This is for convenience: $res will be the output variable of other operations, and we expect normalisation to be the last thing they do.)

    normalise() {
        local i
    
        for (( i = 0; i < ${#res[@]}; i++ )); do
            if (( res[i] >= MAXINT )); then
                let res[i+1]+=(res[i] / MAXINT)
                let res[i]=(res[i] % MAXINT)
            elif (( res[i] < 0 && ${#res[@]} > i+1 )); then
                let res[i+1]-=1
                let res[i]+=MAXINT
            fi
        done
    }

This doesn't handle every case; for example, a term smaller than -MAXINT will break things. But it will be sufficient for our purposes.

With this, addition and subtraction are easy. We only need addition of an int and a bigint, so will call this addi (i for integer) and operate on the variable $op1.

    addi() {
        res=( ${op1[@]} )
        let res[0]+=$1
        normalise
    }

Subtraction needs to be defined between two bigints, but we only need positive results.

    sub() {
        local i
        res=()
        for (( i = 0; i < ${#op1[@]}; i++ )); do
            let res[i]=op1[i]-op2[i]
        done
        normalise
    }

Multiplication and division follow similarly. (We only need to divide a bigint by 10, but allowing an arbitrary int is no harder.)

    muli() {
        local i
        res=(${op1[@]})
        for (( i = 0; i < ${#res[@]}; i++ )); do
            let res[i]*=$1
        done
        normalise
    }
    
    divi() {
        local i
        res=(${op1[@]})
        for (( i = ${#res[@]}-1; i > 0; i-- )); do
            let res[i-1]+="MAXINT*(res[i] % $1)"
            let res[i]/=$1
        done
        let res[0]/=$1
        normalise
    }

(We note that `muli` might break if the multiplicand is close to 2^32: if two adjacent terms in $res are sufficiently large, `normalise` might cause overflows. But we're assuming the multiplicand is at most 2^31 - 1, and testing indicates that this works fine.)

For `modi`, even though the result is a normal integer, we'll return it in $res like a bigint. The other option would be to echo it, but then we'd need to spawn a subshell to use it. (Test this yourself: compare `echo 'echo hi' | strace -f bash` to `echo 'echo $(echo hi)' | strace -f bash`. The first doesn't fork at all, because `echo` is a builtin command; but the second forks a subshell to run `echo hi`.) Forking isn't cheating, but it seems worth avoiding.

    modi() {
        local i
        let res=0
        for (( i = 0; i < ${#op1[@]}; i++ )); do
            let res+="${op1[i]}%$1 * (MAXINT%$1)**i"
        done
        let res%=$1
    }

For division and modulo, we need a ≤ operation; we can use its exit code for the return value. (We return 0 (true) if op1 ≤ op2, and 1 (false) otherwise.)

    le() {
        local i
        local len=${#op1[@]}
        (( len < ${#op2[@]} )) && len=${#op2[@]}
    
        for (( i = len-1; i >= 0; i-- )); do
            if (( op1[i] > op2[i] )); then
                return 1
            elif (( op1[i] < op2[i] )); then
                return 0
            fi
        done
        return 0
    }

Finally we can implement division and modulo. We'll just define a mod operator, which can store the division result in a variable $div.

    mod() {
        local temp=( ${op1[@]} )
        let div=0
        res=( ${op1[@]} )
    
        until le; do
            let div+=1
            sub
            op1=( ${res[@]} )
        done
    
        op1=( ${temp[@]} )
    }

So mod stores $op1 % $op2 in $res, and $op1 / $op2 in $div. Since we know $op1 / $op2 will always be less than 10, we could maybe get a slight speed improvement with a binary search, but I really doubt that's going to be a bottleneck.

It would be foolish not to test these. These Haskell functions (entered into GHCI, which only accepts one-line definitions) will help:

    let x = 2^32
    let splitint n = if n < x then (show n) else (show (n `mod` x)) ++ " " ++ splitint (n `div` x)
    let unsplit s = sum $ map (\(a,b) -> b*x^a) $ zip [0..] $ map read $ words s

`splitint` turns an arbitrary-precision Integer into a string that we can copy into a bash array. `unsplit` does the opposite, taking a space-separated list of integers and turning them into an arbitrary-precision Integer. (Haskell is good for this because it has arbitrary-precision arithmetic. I originally tried this in Python, and wasted a lot of time trying to track down a bug in my bash code before realising that Python was wrong.) So we choose a few arbitrary large numbers and verify that everything works as expected. (Unsurprisingly, I caught a few bugs when I actually tried this.)

Having implemented bigints to the extent necessary, we can hopefully extract more digits from e. Arithmetic is ugly now, so we'll split off some functions, all using variables $a and $b.