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

```sh
fac() {
    if [[ $1 -eq 0 ]]; then
        echo 1
    else
        echo $(( $1 * `fac $(($1 - 1))` ))
    fi
}
```

Since we only have integer division, we obviously can't calculate 1/2!. But note that x/a! + y/(a+1)! = (x(a+1) + y)/(a+1)!. We can use this to recursively calculate (sum 1/k! \[0 ≤ k ≤ n\]) as numer(n)/n!, where numer(0) = 0, numer(k) = k\*numer(k-1) + 1.
