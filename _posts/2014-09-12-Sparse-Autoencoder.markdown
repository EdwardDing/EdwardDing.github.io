---
layout: post
title: "Sparse Autoencoder"
date: 2014-09-07 10:16
excerpt: Programming Assignment 1 of UFLDL - Sparse Autoencoder implementation.
---

{% include custom/mathjax.html %}

For details about `UFLDL`, please check [this wiki](http://deeplearning.stanford.edu/wiki/index.php/UFLDL_Tutorial). You can find this exercise under `Sparse Autoencoder`.

The main difficulty here is the implementation of ***sparseAutoencoderCost.m***, which is the function to calculate the `graditude` of \\(J(W,b)\\) and represent the cost funtion.

You are encouraged to write the code by youself rather than just copy and paste from this blog. Also, if you find any questions or mistakes, feel free to leave your message below.

###Before Coding

---------------------
Here are some basic formula related to the algorithm.

#### ***Basic Cost Funtion***

$$
J(W,b) = \frac{1}{m} \sum_{i=1}^{m} J(W,b;x^{(i)},y^{(i)}) + \frac{\lambda}{2} \sum_{l=1}^{n_l-1} \sum_{i=1}^{s_l} \sum_{j=1}^{s_l+1} (W_{ji}^{(l)})^2
$$

Where:

$$
J(W,b;x^P{(i)},y^{(i)}) = \frac{1}{2}{}\left \| h_{W,b}(x) - y \right \|^2
$$


#### ***Back Propagation Algorithm***
We are using `Back Propagation Algorithm` to calculate the grad. There are 4 steps in the algorithm:

***Step 1:*** Perform a feedforward pass, computing the `activations` for all layers.

***Step 2:*** For each output unit \\(i\\) in layer \\(n_l\\) (the last layer, output layer), set

$$
\delta_i^{(n_l)} = -(y-a^{(n_l)})\bullet  f'(z^{(n_l)})
$$

***Step 3:*** For \\(l = n_l-1,n_l-2,...,2\\)

$$
\delta^{(l)} = ((W^{(l)})^T \delta^{(l+1)}) \bullet  f'(z^{(l)})
$$

***Step 4:*** Compute the partial derivatives:

$$
\begin{align}
\bigtriangledown_{W^{(l)}} J(W,b;x,y) 
&= a_j^{(l)}\delta^{(l+1)} \\
\bigtriangledown_{b^{(l)}} J(W,b;x,y) 
&= \delta^{(l+1)}
\end{align}
$$

where: \\( f'(z^{(l)}) = a^{(l) \bullet (1 - a^{(l)})} \\)

> Note: Be clear with the difference bwtween \\( \bigtriangledown J(W,b;x,y)\\) and \\( \bigtriangledown J(W,b)\\). This algorithm can only calculate the partial derivatives for one given training set. To get the partial derivatives for the whole training set, we need to do some extra calculation as below.

$$
\begin{align}
\frac{\partial}{\partial W_{ij}^{(l)}} J(W,b) 
&= \frac{1}{m}\sum_{i=1}^{m} \frac{\partial}{\partial W_{ij}^{(l)}} J(W,b;x^{(i)},y^{(i)}) +\lambda W_{ij}^{(l)} \\
\frac{\partial}{\partial{b_{i}^{(l)}}} J(W,b) 
&= \frac{1}{m}\sum_{i=1}^{m} \frac{\partial}{\partial b_{i}^{(l)}} J(W,b;x^{(i)},y^{(i)})
\end{align}
$$


#### ***Sparse Autoencoder***
As we want to implement the `Sparse Autoencoder`, we need to add the `penalty term`, so the formula for the cost function and the derivative need to be modified as :

$$
J_{sparse}(W,b) = J(W,b) + \beta\sum_{j=1}^{s_{2}}KL(\rho\parallel\hat{\rho_{j}})
$$

In the formula, \\( \rho \\) is called `Sparsity Parameter`, usually we set it to 0.001. \\( \hat{\rho_j} \\) is defined as the average of all activations of j-th unit in the hidden layer caused by m training sets.

$$
\hat{\rho_j} = \frac{1}{m} \sum_{i=1}^{m} a_j^{(2)}(x^{(i)})
$$

`KL divergence` is a way to represent the difference between two distributions. Here we just need to know how to calculate it and know that the KL divergence is 0 when the two distributions are exactly the same, and increase to \\( +infty \\) when they are quite different.

$$
KL(\rho\parallel\hat{\rho_{j}}) = \rho log \frac{\rho}{\hat{\rho_{j}}} + (1-\rho)log \frac{1-\rho}{1-\hat{\rho_{j}}}
$$


###Implementation

--------------------
The input are 10 512\\(\times\\)512 images after `whiten` process. Here is what it looks like:

<div style="text-align:center">
	<a>
		<img src = "/assets/SparseAutoencoder/input4.jpg" alt = "input4">
	</a>
</div>

First we need to load the picture, randomly select 10,000 8\\( \times \\) 8 patches from the input data and reshape them into a 64 \\( \times \\) 64 matrix. This should be easy, we need to implement it in ***sampleIMAGES.m***.

{% highlight matlab %}
for i = 1:numpatches
    % Generate random integer for x, y, and pic_num
    x = randi(512 - patchsize);
    y = randi(512 - patchsize);
	 pic_num = randi(10);
    
	 one_patch = IMAGES(x:x+patchsize-1,y:y+patchsize-1,pic_num);
    patches(:,i) = reshape(one_patch, patchsize * patchsize, 1);
end
{% endhighlight %}


The `Normalization Porcess` has been implemented, we will just leave them.

Run `sampleIMAGES`, which will take under 5 seconds if everything is OK. And the output should be something like this:

<div style="text-align:center">
	<a>
		<img src = "/assets/SparseAutoencoder/imageSample.jpg" alt = "imageSample">
	</a>
</div>

After that, we need to add a function to implement gradient check. The basic idea is that the `Numerical Gradient` should be near to the result we get from iteration. Add some lines in ***computeNumericalGradient.m***, here is my implementation:

{% highlight matlab %}
EPSILON = 1.0e-4;

for i = 1:size(theta)
    eps = zeros(size(theta));
    eps(i) = 1;
    numgrad(i) = (J(theta + eps * EPSILON) - J(theta - eps * EPSILON)) / (2 * EPSILON);
end
{% endhighlight %}

Run `checkNumericalGradient` which has been writen for you, to check whether your funcion to compute the numerical gradient is correct. You should get something like:

<div style="text-align:center">
	<a>
		<img src = "/assets/SparseAutoencoder/check.png" alt = "check">
	</a>
</div>

Ok, all preparations are ready, it's time heading for the most important function in ***sparseAutoencoderCost***. Algorithm and formulae all have been mentioned above, all you need to do is to write them in the syntax for Matlab.

> Tips: The objective \\( J_{sparse}(W,b) \\) contains 3 terms, cirresponding to ***the squared error term, the weight decay term and the sparsity penalty***. You can implement the cost function and derivative computation only for the squared error term first by setting \\( \lambda = \beta \ 0 \\). Only after you've verified that your code of `Back Propagation` is working, add in code to compute the weight decay and sparsity penalty terms.

When you finish, the error should be less than \\(1.0e-9\\):

<div style="text-align:center">
	<a>
		<img src = "/assets/SparseAutoencoder/error.png" alt = "error">
	</a>
</div>

{% highlight matlab %}
m = size(data, 2);

% Step1: feedforward
z2 = W1 * data + repmat(b1,1,m);
a2 = sigmoid(z2);
z3 = W2 * a2 + repmat(b2,1,m);
a3 = sigmoid(z3);

% Calculate the Sum of KL Divergence of rho and SparsityParam
rho = sum(a2,2) ./ m;
kl_divergence = sparsityParam * log(sparsityParam ./ rho) + (1 - sparsityParam) * log ((1 - sparsityParam) ./ (1 - rho)); 

cost = 1/m * (1/2 * sum(sum((a3 - data).^2))) + lambda/2 * (sum(sum(W1.^2)) + sum(sum(W2.^2))) + beta * sum(kl_divergence);

Calculate each Partial J(W,b,x,y) to get Partial J(W,b)
for i = 1:m
    
    y = data(:,i);
    % Step2: calculate delta_3
    diff_n = a3(:,i) .* (1 - a3(:,i));
    delta_3 = -(y - a3(:,i)) .* diff_n;

    % Step3: calculate other delta_l, here we only have delta_2
    diff_2 = a2(:,i) .* (1 - a2(:,i));
    delta_2 = (W2' * delta_3 + beta * (-sparsityParam ./ rho + (1 - sparsityParam) ./ (1 - rho))) .* diff_2;

    % Step4: calculate all grad
    W1grad = W1grad + delta_2 * data(:,i)';
    W2grad = W2grad + delta_3 * a2(:,i)';
    b1grad = b1grad + delta_2;
    b2grad = b2grad + delta_3;

end
{% endhighlight %}

This code should run about 10 minutes. To speed up a little bit, you can `vectorize` the loop in you code.

{% highlight matlab %}
% vectorize
y = data;
% Step2: calculate delta_3
diff_n = a3 .* (1 - a3);
delta_3 = -(y - a3) .* diff_n;

% Step3: calculate other delta_l, here we only have delta_2
diff_2 = a2 .* (1 - a2);
delta_2 = (W2' * delta_3 + repmat(beta * (-sparsityParam ./ rho + (1 - sparsityParam) ./ (1 - rho)),1,m)) .* diff_2;

% Step4: calculate all grad
W1grad = W1grad + delta_2 * y';
W2grad = W2grad + delta_3 * a2';
b1grad = b1grad + sum(delta_2,2);
b2grad = b2grad + sum(delta_3,2);
%

W1grad = W1grad / m + lambda * W1;
W2grad = W2grad / m + lambda * W2;
b1grad = b1grad / m;
b2grad = b2grad / m;
{% endhighlight %}

This time, your code should be a little  bit faster.

Now, we've implemente the function for calculating the cost and the derivative. A good news is you don't need to implement the iteration by yourself. It has been provided for you in ***/minFunc***. We are using `L-BGFS Algorithm` here, whose speed of convergence is very high.

No more work for us, all we need to do now is to run `train`. After minutes of calculation, the result pops up.

<div style="text-align:center">
	<a>
		<img src = "/assets/SparseAutoencoder/result.jpg" alt = "result">
	</a>
</div>

Well done!

You can find my source code [here](https://github.com/EdwardDing/UFLDL-Exercise) under SparseAutoencoder folder.