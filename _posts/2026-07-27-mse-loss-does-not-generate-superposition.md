---
title: MSE loss does not generate superposition
layout: post
tags: [math]
external_comments:
  - name: LessWrong
    url: https://www.lesswrong.com/posts/cfwAK4Qvjne4RjB74/mse-loss-does-not-generate-superposition
---

*Co-authored with [Linda Linsefors](https://www.lesswrong.com/users/linda-linsefors)*

If you're training any type of toy model of superposition, Mean Squared Error (MSE) loss is unusually bad.[^superposition]

[^superposition]: Superposition is a fuzzy concept, with no precise consensus definition. We mean that each feature is encoded linearly, using almost orthogonal direction. But actually, for this post it's enough to say that it's definitely not superposition if all feature embeddings are exactly orthogonal, or if any two feature embeddings are identical. For the purpose of this post, we'll consider everything else "superposition".

    Even with this overly broad definition, we'll still show that MSE Loss doesn't favor superposition over non-superposition.

# Related work

We aren't the first to notice that MSE loss doesn't work. In [Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model/index.html) the effective loss function is $\mathrm{MSE}(\mathrm{ReLU}(\mathrm{target} - \mathrm{model\\_output}))$, because they noticed that plain $\mathrm{MSE}(\mathrm{target} - \mathrm{model\\_output})$ doesn't work.

More recently [Compressed Computation Under $L^4$ Loss is Likely Computation in Superposition](https://www.lesswrong.com/posts/cTRKj3giaZN5Ysyx2/compressed-computation-under-l-loss-is-likely-computation-in) again demonstrated that MSE loss dosn't work. MSE loss is the same as $L^2$ loss[^same], because MSE is just the square of the $L^2$ norm. The above mentioned paper showed that $L^{2.5}$, $L^{3}$, $L^{4}$, $L^{6}$, $L^{8}$ all worked to produce superposition encodings, but $L^2$ doesn't.

[^same]: They have the same minimum, and the gradient is always in the same direction, so they're functinally the same under gradient descent. 

Why this post then? Given that the core claim is already thoroughly demonstrated? Two reasons:

1. I (Linda) read *Toy Models of Superposition* too long ago to remember this result.
2. *Compressed Computation Under $L^4$ Loss* came out after this post was almost done.

Which resulted in me (Linda) using MSE loss in attempted superposition toy experiments. I learned for myself that it doesn't work, did a bunch of math with Phil to prove why it doesn't work, and therefore this post. 

***If you are satisified with the previous results on this topic, no need to read any further.***

# Core Claim

Suppose you want to train a neural network to encode more features than it has neurons. If you train this network using MSE loss on these features, the network is not incentivized to encode them in superposition. So if there's anything else going on in the experiment that may push the solution towards non-superposition, you're most likely going to end up with non-superposition. This can be an issue when trying to do toy models specifically of superposition. One of us (Linda) has run into this problem. 

**However, the solution is easy:** Don't use MSE loss, instead use some other loss instead. If cross-entropy loss is not applicable, you can use $\mathrm{loss}\\!=\\!\mathrm{mean}\left(\mathrm{error}^4\right)$
instead of $\mathrm{loss}\\!=\\!\mathrm{mean}\left(\mathrm{error}^2\right)$.

In this post we pressent three lines of evidence for this claim: 

1. Linda has run into this problem;
2. Toy model experiments;
3. Math.

We consider the math to be the strongest evidence for our claim, becuase the best way to know if something generalises is to do the math. But the math section is also the longest and the densest part of the post, which is why it's pressented last.

## Caveat

MSE loss will not push towards superposition, but nor will it always push against superposition. If you're using random initialization, you may sometimes get (something like) superposition, just from your starting conditions.

E.g. One toy model of Compressed Computation looked like it was performing computation in superposition, untill [closer investigation](https://www.lesswrong.com/posts/ZxFchCFJFcgysYsT9/compressed-computation-is-probably-not-computation-in#x8amYydvZyJKNCqmC). 

# Initial Observations

This is the backstory for why we ended up doing all the investigations that follow in the rest of this post.

I (Linda) was doing some [computation-in-superposition](https://www.lesswrong.com/w/comp-in-sup) toy model experiments. In these experiments, a neural network was trained to represent more tiny circuits than it had hidden layer neurons (but it would only have to compute one or very few circuits in any single forward pass). In these experiments, I also introduced noise in the input.[^2] I had the hypothesis that introducing noise to the input would reduce the number of neurons used per circuit, since that would reduce the amount of noise passing through the network and ending up in the output.[^3]

[^2]: This was to simulate being in the middle of a network, where I expect input features to be some amount of noisy, due to superposition compression in previous layers.

[^3]: I (Linda) have used this trick for noise reduction myself in the construction here: [Circuits in Superposition 2: Now with Less Wrong Math](https://www.lesswrong.com/posts/FWkZYQceEzL84tNej/circuits-in-superposition-2-now-with-less-wrong-math).

I was right! Introducing noise did cause the network to distribute each circuit over a much smaller number of neurons. 

However, I had expected the network to come to some trade-off between using more neurons per circuit, in order to get more superposition (to maintain it's ability to tell different circuits apart), and fewer neurons per circuit, in order to get less noise. Instead the network just went for (close to) as few neurons as it could, and did not seem to care about maintaining superposition. 

So then I went on a side quest to find out why, which much later[^4] became this post.

[^4]: Most of the delay was me pursuing other research projects.

Another in-the-wild observation is [this project](https://www.lesswrong.com/posts/ZxFchCFJFcgysYsT9/compressed-computation-is-probably-not-computation-in), which found that another intended-to-be toy model of superposition, also trained with MSE loss, was (probably) not actually superposition.

# General setup for both the Experiments and Math

Imagine you're training a neural network. At the last hidden layer of the model, you'd like to incentivise the network to represent the final output in superposition.

The last hidden layer has $D$ neurons, and the output has $T$ features where $T$ is larger than $D$. Each feature can either be active, represented by $1$, or inactive, represented by $0$. There are at most $z$ active features at any one time.

In this post, we're not concerned about how the last hidden layer is computed. Imagine that some network has enough layers or whatever it needs to produce the optimal encoding for its output features in the final hidden layer. What we want to find out is, what's the best possible encoding the network can use, just before the readout, given the bottlneck $D<T$? The way we investigate this in practice (both in the experiments and the math), is to feed the desired output as input, into a single hidden layer of dimension $D$.

Typically in superposition one also assumes that the features only activate sparsely. In this post we'll assume that at each forward pass, exacty $z$ features are active, for some small value of $z$.[^small-z]

[^small-z]: We don't use the assumption that $z$ is small for anything. But this is the setting where one might expect superposition, which is why that's the main focus of this post.

We also assume that every allowed output (given $T$ and $z$) is equally likley.

Then, given $T$, $D$, $z$ and some specific loss function, what is the optimal feature embedding? I.e. what should the last layer activations be, as a function of the set of active features, in order to minimise the loss?


# Experiments

## Setup

We train a linear [autoencoder](https://en.wikipedia.org/wiki/Autoencoder) to embed and then unembed $T$ features, into $D$ neurons and then back into $T$ features again. The input is a $T$-dimensional $z$-hot vector, and the target is always the same as the output. We train each network on a dataset of every possible such feature vector.

**Code for the model:**
```python
class FeatureCompressionModel(torch.nn.Module):
    def __init__(self, T, D):
        super(FeatureCompressionModel, self).__init__()
        self.encode = torch.nn.Linear(T, D, bias=False)
        self.decode = torch.nn.Linear(D, T, bias=False)
        self.D = D
        self.T = T
        self.bias = bias

    def forward(self, x):
        x = self.encode(x)
        x = self.decode(x)
        return x
```

**Code for generating the training data:**

```python
if z == 1:
    data = torch.eye(model.T, device=next(model.parameters()).device)
elif z == 2:
    data = []
    for i in range(model.T):
        for j in range(i+1, model.T):
            one_data=torch.zeros(model.T)
            one_data[i] = 1
            one_data[j] = 1
            data.append(one_data)
    data = torch.stack(data, dim=0)
```

We then trained these models using four different loss functions:
* MSE:    `loss = torch.nn.MSELoss()(outputs, targets)`
* BCE ("binary cross-entropy"):    `loss = torch.nn.BCEWithLogitsLoss()(outputs, targets)`
* L4:        `loss = torch.mean((outputs - targets)**4)`
* CE ("cross-entropy"):        `loss = torch.nn.functional.cross_entropy(outputs, targets.argmax(dim=-1))`

We're testing:
* $D=2$[^D2]
* $T=3$, $4$ or $5$[^T345]
* $z=1$ or $2$[^z12]


Finally we plot the embedding vectors.

[^D2]: We use $D=2$ for all experiments, because it's the only value for $D$ that's easy to visualise.

[^T345]:For this to be any interesting we need $T$ to be larger than $D$, i.e. larger than $2$. The numbers $3, 4$ and $5$ are some nice numbers that are all larger than $2$.

[^z12]:There are several reasons to prefer $z=1$: 
    * Typically in superposition it's assumed that $z < D$. With $D=2$ this requires $z=1$. 
    * We have an exact formula for $\mathrm{MSE}_\mathrm{orth}$ only in the case of $z=1$.
    * CE loss only works for $z=1$. This loss function assumes only one true answer and is not well defined for other values of $z$.
    * Earlier in the post we said that we're interested in the setup where the readout needs to be linear, but that the encoding can be any function of the input. For $z=1$, and only $z=1$, every embedding can be written as a linear function. So we get the fully general case with a very simple model. (It happens to be the case that all the encodings described in the math section can be done using a linear embedding for any $z$, but that wasn't an intentional restriction.)

    But despite this list of reasons for $z=1$, we also did one experiment with $z=2$, because why not.

## Results
We trained models with each of [T=3, D=2, z=1], [T=4, D=2, z=1], [T=5, D=2, z=1] and [T=5, D=2, z=2], on the four different loss functions (MSE, BCE, L4 and CE), five times each. The embeddings of the trained models are visualised below.

By default embedding vectors are green. But small embeddings are yellow (norm is less than 20% of the largest one) and very small ones are red (norm is less than 10% of the largest one).

Dotted green lines are the negative of the embedding vectors.

<a href="https://hackmd.io/_uploads/HJf5lXSaWx.png"><img src="https://hackmd.io/_uploads/HJf5lXSaWx.png" style="width:95%" alt="T3_D2_z1_withCE"></a>

<a href="https://hackmd.io/_uploads/BJkDl7HaZg.png"><img src="https://hackmd.io/_uploads/BJkDl7HaZg.png" style="width:95%" alt="T4_D2_z1_withCE"></a>

<a href="https://hackmd.io/_uploads/HyyPlQB6Zx.png"><img src="https://hackmd.io/_uploads/HyyPlQB6Zx.png" style="width:95%" alt="T5_D2_z1_withCE"></a>

<a href="https://hackmd.io/_uploads/rJ1De7rTZe.png"><img src="https://hackmd.io/_uploads/rJ1De7rTZe.png" style="width:95%" alt="T5_D2_z2"></a>

Superposition here looks like "vectors and their negations being far away from each other". And just as we claim, MSE loss does not consistently produce superposition: it's common for vectors to be nearly on top of each other. Our math (next section) suggests that no embedding should be prefered over any other embeding when when using MSE loss (at least for $z=1$). The results seem to confirm this, since the MSE embeddings are very varied. 

For z=1, MSE is the only loss function that does not produce a clear pattern in how the embeddings look. For z=2, they're all a bit wonky.

Networks trained with BCE loss are doing well at producing superposition for [T=3,D=2,z=1], but "give up" for larger T, and instead just represent two features approximately orthogonally, and don't represent the others. This is probably because positive interference is particularly bad for BCE. But I (Linda) am still a bit suprised it didn't manage to do something more like superposition for [T=3,D=2,z=1].

Networks trained with L4 loss avoid negative correlations as much as they avoid possitive correlation. This is expected, since L4 loss penalises negative and positive interference equally. This is also true for MSE loss, but it's less obvious in the results, because MSE loss is just all over the place with no clear pattern.

Networks trained with CE loss are arguably doing best in terms of producing superposition, with the main drawback that this loss is only applicable for z=1.

# The Math 
If you want to know if something generalises, it's best to do the math.

In this section, we do a lot of math that does not quite prove the core claim, but shows that it's probably true.

We consider the math in this section to be our main result, and the strongest evidence for our claim at the start of the post. When working on this project, we did the math first, and only later did the experiment to confirm our conclusions. 

## Setup

Since you've made it here we assume you like math. So we'll define the general setup again, now using math notation.

You're trying to implement (or at least closely approximate) some function with a neural network. The functions we're looking at here have output type $\\{0,1\\}^T$ (i.e. they output a $T$-dimensional vector of $1$s and $0$s) where at most $z$ of the output values are $1$. The network's final hidden layer has $D$ neurons, and the network's approximation of the answer is read out as some linear function of the final layer.

We're interested in questions of whether and how networks can encode certain information, so the function you're trying to implement doesn't matter. For simplicity, we'll say it's the identity function: your network takes a vector of $T$ binary inputs (where at most $z$ of the inputs are $1$), and spits out $T$ real outputs, and is trying to reproduce the input as closely as possible.

(This function is the best case scenario, in some sense. Whatever the best-possible performance is on the identity function, it must be at least as good as the best-possible performance on any other function, with caveats around frequency of results.)

That means we can split your function into two: the part that computes the final hidden layer, and the part that reads out the result from that. We're not worried about the limitations of the first function, so we'll say it can be anything at all, regardless of how easily it can be implemented with a neural network.

As another simplification, we'll say that *exactly* $z$ of the inputs will be $1$, not *at most* $z$.

And so our moving parts are:
* We have a random vector $y$ of $T$ binary inputs, where exactly $z$ of them are $1$ and the rest $0$.
* This feeds into a vector $e = f(y)$ of $D$ neurons, where $f:\\{0,1\\}^T → ℝ^D$ is some function we get to choose how we like.
* Then we read a vector $\hat{y} = g(e)$ of $T$ estimates, where $g:ℝ^D → ℝ^T$ is some *linear*[^linear] function that we also get to choose.

[^linear]: We could also allow the function to be [affine](https://en.wikipedia.org/wiki/Affine_transformation) (i.e. "linear plus some constant"). The difference between linear and affine is going to be small for large D, because if the constant is helpful, you can just sacrifice a neuron to get it (the "augmented matrix" representation).

Our expected loss is
$$\mathrm{MSE} = 𝔼_y \left( \frac{1}{T}\sum_{i=1}^T (\hat{y}_i - y_i)^2 \right).$$

So the question is: what are some ways we can choose $f$ and $g$, and what losses do they give us?

## One feature per neuron

In this encoding, each neuron simply represents a single feature. Since there are fewer neurons than features, that means some features don't get represented. For represented features, we know exactly whether they were active or not; for the others, we simply guess that they weren't.

So our estimates will be

* $\hat{y}_i = y_i$, for the $D$ features that are represented;
* $\hat{y}_i = 0$, for the $T-D$ other features.

So all the loss is going to come from the unrepresented features. The number of unrepresented features is $T-D$ and the probability of a feature being activated is $z \over T$. The activated unrepresented features give loss $1$ and the nonactivated unrepresented features give loss $0$.

So ultimately,

$$ \mathrm{MSE}_\mathrm{1fpn} = {1 \over T} {z \over T}(T-D) = {z \over T}\left(1 - {D \over T}\right). $$

We can probably slightly improve on this for $z > 1$. The current loss is good enough for this post, but details in footnote[^1fpn-improvement].

[^1fpn-improvement]: First, note that if we allowed affine readouts, then our estimate for unrepresented features could be $$\hat{y}_i = a$$, for some constant $a$. We'd choose $a$ to trade off between "false positives" and "false negatives"; the optimal choice is $$a = {z \over T}$$, which gives $$\mathrm{MSE}_\mathrm{1fpn} = z\left(1 - {D \over T}\right)\left(1 - {z \over T}\right)$$.

    With linear readouts, we don't have that constant. But $$\sum_{j=1}^D e_j$$ is linear, and lies between $0$ and $z$. So we could set $$\hat{y}_i = a'\sum_{j=1}^D e_j$$, for some constant $a'$.
    
    This doesn't help for $z=1$. If $\sum_{j=1}^D e_j = 1$, then we know the active feature is represented, and we want to predict the unrepresented features as $0$; if it's $0$, then we know the active feature is unrepresented, but we have no way to predict the unrepresented features as anything except $0$.
    
    But it seems like it should help for higher $z$. There's still an awkward tradeoff that the fewer active unrepresented features there are, the higher we'll predict them. But consider $z=2$. Our loss from the unrepresented features will be: 
    
    * With probability $\left(D \over T\right)^2$, both active features are represented; our loss will be $(T-D)(2a')^2$.
    * With probability $\left(D \over T\right)\left(1 - {D \over T}\right)$, one active feature is represented; our loss will be $(T - D - 1)a'^2 + (1 - a')^2$.
    * Otherwise, no active features are represented but $\sum_{j=1}^D e_j = 0$, so our loss will definitely be $2$.
    
    So we minimize total expected loss at $a' = {1 \over 3D + T}$.
    
    We're not going to bother getting a closed-form solution for MSE with this adjustment, but it'll be a mild improvement.

## One neuron per feature

Next, we could give every feature a neuron. That means some neurons represent multiple features, and our estimates won't be able to distinguish them. On average, each neuron will represent $T \over D$ features.

Since $z$ is small, "two active features being represented by the same neuron" is unlikely. We'll assume it's unlikely enough not to change the MSE much, and pretend for now it can't happen. (For $z=1$ it actually can't happen.)

Here the loss is all going to come from active output features. We'll have $zT \over D$ features that may have been activated, and the rest we know won't be. For example, this might concretely be implemented as

$$ R_{i,j} = \cases{1 & neuron $j$ represents feature $i$ \\ 0 & otherwise}$$

$$ e_j = \sum_{i=1}^T R_{i,j}y_i $$

$$ \hat{y}_i = a \sum_{j=1}^D R_{i,j}e_j $$

So that $e_j$ is "the number of active features that this neuron represents" (and $\sum_{j=1}^D e_j = z$), and each $e_j$ is either $0$ or $1$).

Each $\hat{y}_i$ is either $0$ or $a$. We can split $\hat{y}$ into three parts:

* Exactly $z$ elements where $y_i = 1, \hat{y}_i = a$, each giving loss $(1-a)^2$. (These are roughly "true positives", but they still have some loss because the network isn't confident they're true.)
* On average, $z\left({T \over D}-1\right)$ elements where $y_i = 0, \hat{y}_i = a$, each giving loss $a^2$. (These are roughly "false positives".)[^t-over-d-noninteger]
* And the rest have $y_i = 0, \hat{y}_i = 0$, giving no loss.

[^t-over-d-noninteger]: This isn't quite right when $T \over D$ isn't an integer. There'll be some neurons corresponding to $\left\lfloor {T \over D} \right\rfloor$ features and some corresponding to $\left \lceil {T \over D} \right \rceil$ features. The latter neurons activate more often, and they have higher loss when one of their features is active. This shouldn't make much difference when $T \over D$ is large, and it's possible to push back against this effect by picking different values of $a$ for the different groups. Linda actually calculated it out and showed that we ultimately get the same loss. But the math for that is a bit messier, so we ignore it here.

So average expected loss is

$$ \mathrm{MSE}_\mathrm{1npf} = {1 \over T}z\left(\left(1-a\right)^2 + \left({T \over D}-1\right)a^2\right) $$

minimized at $a = {D \over T}, 1 - a = {T - D \over T}$, giving

$$ \mathrm{MSE}_\mathrm{1npf} = {z \over T}\left(1 - {D \over T}\right). $$

Same as we got for "1 feature per neuron"! We'll call these embeddings "orthogonal", and use the symbol $\mathrm{MSE}_\mathrm{orth}$ for their loss.

Again, if $z>1$, we can get a slight improvement by relaxing the "only one active feature per neuron" assumption. Discussion is delegated to footnote[^1npf-improvement].

[^1npf-improvement]: If we accept that multiple active features might be assigned to the same neron, that complicates the analysis in two ways. First, there are fewer "false positives", which gives a decrease in loss. Second, some of the $e_j$ come out as 2 or higher, which has unclear effects on loss.

    But since $f$ can be any arbitrary function, we can instead set
    
    $$ e_j = \min\left(1, \sum_{i=1}^T R_{i,j}y_i\right) $$
    
    and the second complication disappears. So our MSE would end up being slightly better than we calculated.
    
    This new function is somewhat harder for "all-but-the-final-layer of a neural network" to implement.
    
    Note: we don't claim this new function is optimal. It's probably not. It might not even be an improvement on the simple $e_j = \sum_{i=1}^T R_{i,j}y_i$. What we claim is that for $z>1$, when we take into account "multiple active features might be assigned to the same neuron", this new function gives us MSE lower than ${z \over T}\left(1 - {D \over T}\right)$.


## Superposition

Here we say that each feature feeds into several neurons, and each neuron has several features feeding into it.

For each feature, we pick a random unit vector $v_i ∈ ℝ^D$. In high-dimensional spaces, most random vectors are approximately orthogonal, so $v_i · v_j ≈ 0$ for $i ≠ j$. We sum the active features' unit vectors into the embedding.

We think this is a close-to-optimal implementation of superposition, but we don't prove that here.

So we have

$$e = \sum_{i=1}^Ty_iv_i$$

$$\hat{y}_i = a(e·v_i)$$

where we pick $a$ to minimize loss. This works (to the extent that it does) because $e · v_i = \sum_{j=1}^Ty_j(v_j·v_i)$; the terms of this sum other than $j=i$ are all approximately $0$, so $\hat{y}_i ≈ ay_i$.

The loss from each inactive feature is $\varepsilon_0$, and from each active feature is $1 - (a + \varepsilon_1)$, where $\varepsilon_•$ are error terms that come from the $v_j$ not being fully orthogonal. Known theorems about random unit vectors give us

$$𝔼(\varepsilon_0) = 𝔼(\varepsilon_1) = 0$$

$$𝔼(\varepsilon_0^2) = za^2/D$$

$$𝔼(\varepsilon_1^2) = (z-1)a^2/D.$$

Then the total loss is

$$\begin{aligned} \mathrm{MSE}_\mathrm{rand\_sup} &= \frac{1}{T}𝔼\Big(z(1 - (a + \varepsilon_1))^2 + (T - z)\varepsilon_0^2\Big) \\ &= \frac{z}{T}\left((1-a)^2 + (T-1){a^2 \over D} \right) \end{aligned}$$

This is minimized at $a = {D \over T+D-1}$, ultimately giving

$$\mathrm{MSE}_\mathrm{rand\_sup} = \frac{z}{T}\left(1 - {D \over T + D - 1}\right).$$

Clearly $${D \over T + D - 1} < {D \over T},$$ which gives us $$\mathrm{MSE}_\mathrm{orth} < \mathrm{MSE}_\mathrm{rand\_sup}$$.

A question remains: whether random embeddings are really a good representation of superposition. Since we defined superposition to be almost anything except the two previous embedding schemas, can't we do better than random? The answer to this is yes, as we'll see in the next two sections.

## z=1, D=2, T=3

Notice that all the calculations for $\mathrm{MSE}_\mathrm{rand\\_sup}$ are exact, and not just some large limit result. So we can check the smallest possible case to see if there's a better option for superpositional embedding.

In the case $z=1$, $D=2$, $T=3$, it sems clear that the best superposition embedding should be the vertices of an equilateral triangle:

$$v_1 = (1,0)$$

$$v_2 = \textstyle{\left(-\frac{1}{2},\frac{\sqrt{3}}{2}\right)}$$

$$v_3 = \textstyle{\left(-\frac{1}{2},-\frac{\sqrt{3}}{2}\right)}$$

With $(v_i · v_j)_{i ≠ j} = - {1 \over 2}$. Using the embedding schema from before, if feature $j$ is activated then $\hat{y}_i = a(v_i · v_j)$, and so the active feature has loss $(1-a)^2$ and the two inactive features have loss $\left({a \over 2}\right)^2$. That gives us

$$ \mathrm{MSE}_\mathrm{best\_sup} = \frac{1}{3}\left( (1-a)^2 + 2\left(\frac{a}{2}\right)^2\right) = \frac{1}{3}\left((1-a)^2 + \frac{1}{2}a^2\right)$$

which is minimised at $a=\frac{2}{3}$, and so

$$ \mathrm{MSE}_\mathrm{best\_sup} = {1 \over 9},$$

which is indeed better than

$$\mathrm{MSE}_\mathrm{rand\_sup} = \frac{z}{T}\left(1 - {D \over T + D - 1}\right) = \frac{1}{6}.$$

We conclude that in this case (and by extension, in general) it is possible to do better than choosing the embedding vectors at random. But what really matters is whether the best-case superposition beats the other embedding options. And no, they turn out to have exactly the same loss:

$$
\mathrm{MSE}_\mathrm{orth} = 
\frac{z}{T}\left(1 -\frac{D}{T}\right) = \frac{1}{9}
$$


## z = 1, D = 3, T = 4

Let's test one more example. In this case the best embedding would be the vertices of a regular tetrahedron:

$$v_1 = (0, 0, 1)$$

$$v_2 = \textstyle{\left({2\sqrt{2} \over 3}, 0, -{1 \over 3}\right)}$$

$$v_3 = \textstyle{\left(-{\sqrt{2} \over 3}, {\sqrt{6} \over 3}, -{1 \over 3}\right)}$$

$$v_4 = \textstyle{\left(-{\sqrt{2} \over 3}, -{\sqrt{6} \over 3}, -{1 \over 3}\right)}$$

with $(v_i · v_j)_{i ≠ j} = - {1 \over 3}$.

Same reasoning as before. If feature $j$ is activated then $\hat{y}_i = a(v_i · v_j)$, and so the active feature has loss $(1-a)^2$ and the three inactive features have loss $\left({a \over 3}\right)^2$. We minimize MSE at $a = {3 \over 4}$, giving

$$\mathrm{MSE}_\mathrm{best\_sup} = \frac{1}{4}\left( (1 - a)^2 + {a^2 \over 3}\right) = {1 \over 16}$$

which again matches 

$$
\mathrm{MSE}_\mathrm{orth} = 
\frac{z}{T}\left(1 -\frac{D}{T}\right) = \frac{1}{16}
$$

So even the best version of superposition is still no better than the orthogonal embeddings, for these values. We expect this to generalize, but do not have a mathematical proof.[^proof-by-physicist]

[^proof-by-physicist]: One of my (Linda's) undergraduate physics teachers called this sort of thing "Proof by Physicist". You test your conjecture for some small values that are easy to check, and if it works, you assume you're correct. Although this method is probably more reliable if you already know that you're right, e.g, because you're teaching a physics undergraduate course, where everything is long established facts.

## Math Discussion

Our proof is incomplete in a handful of ways.

* For $z=1$, we got an exact result for $$\mathrm{MSE}_\mathrm{1fpn}$$, but our result for $$\mathrm{MSE_{1npf}}$$ assumed $$T \over D$$ was large or an integer.
* For $z>1$ we didn't get exact loss values for our orthogonal embeddings; but the loss will be lower than the calculated values, which strengthens the result.
* We assumed that random vectors were a good implementation of superposition, even though we managed to improve on them for some specific values.
* We also didn't investigate what happens if fewer-than-$z$ features are allowed to be active.

For $z=1$, we suspect that the optimal MSE loss will be the same for every embedding, regardless of $T$ and $D$, as long as the embedding is using all the neurons[^all-neurons], and as long as the unembedding is tuned optimally for every feature. (Opus has a [claimed proof](https://claude.ai/share/1facd55e-0afb-49a9-bbef-01456e6efe29) but we haven't looked at it in enough depth to trust.)

[^all-neurons]: To be precise, for $z=1$ any embedding function is linear, so "using all the neurons" means the embedding matrix is rank $D$.

Why? Because it would be surprising if both (what we call) "the best" superposition solution, and the two orthogonal solutions, would all be ideal; but nothing in between is as good.

But if so, why is $$\mathrm{MSE}_\mathrm{best\_sup}$$ better than our result for $$\mathrm{MSE}_\mathrm{rand\_sup}$$? We think because we picked a single value of $a$ for our superposition unembeddings. "The best" superposition is symmetrical, so using the same $a$ for all features is correct. But a random embedding won't be symmetrical. Some features will be closer to others and would ideally have a lower $a$, while more lonely features will ideally have a higher $a$, but we didn't tune them. This rhymes with the discussion of "what if $T \over D$ isn't an integer" in footnote[^t-over-d-noninteger].

We don't think every embedding is exacly equal for $z\geq2$.
