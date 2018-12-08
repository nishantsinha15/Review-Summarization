# Review-Summarization
Course Project NLP

## Introduction 
E-commerce websites like Amazon are filled with too many reviews for every product. As the number of reviews grow for a product, it becomes hard for the buyers to decide whether or not to buy the product, as they can't possibly go through all the reviews. We aim to produce feature based positive and negative opinions for a product based on all the reviews for that product.
For e.g. for a digital camera, we can show the count of positive and negative reviews along with the reviews for the feature picture quality etc.  
   
## It involves three major sub-tasks given as follows:  
1. Identifying features of the product that customers have expressed their opinions on(aka product features)
2. For each feature, identifying positive or negative opinions
3. Producing a summary using the information collected from 1. and 2.  
    
## Dataset

We are using the Amazon data-set with reviews restricted to the Electronics category with products having at least 5 reviews (5-core).  
Source: \url{http://jmcauley.ucsd.edu/data/amazon/}  
The data-set contains 7,824,482 reviews. Each review contains details about the reviewer, time of posting, title, text, helpfulness and rating. However, this corpus is untagged. Hence, we will be only trying unsupervised techniques towards summarization.  
  
To evaluate each step of the pipeline, we use different datasets, which are labeled. This is done also because we would like to compare with the methods already described in previous works.  

## Model

### Model Pipeline  

We are extending the work from Mining and Summarizing Customer Reviews by Minqing Hu and Bing Liu, 2004 by making stepwise improvements. 
The authors divide the entire task in three steps:
1. Mining product features that have been commented on by customers.
2. Identifying opinion sentences in each review and deciding whether each opinion sentence is positive or negative
3. Summarizing the results   

This neatly divides our implementation into 3 major portions - Aspect detection, sentiment analysis and summary generation.

# 1. Aspect Identification
For baseline, we created a LDA model where each sentence is treated as a separate document. This is to look for overarching themes in multiple reviews rather than grouping a set of reviews.

LDA is a generative model where each word in a document is assumed to be generated from a mixture of topics. The topics are assumed to follow a sparse Dirichlet prior.


# 2. Sentiment Analysis
We have used the criteria of declaring a review positive if it's rated overall greater than 4.0 and we assume a review to be negative if the user rates the item overall less than 2 to compare our predictions. 

We also tried the dictionary tools based approach on other datasets including IMDB movie reviews and Yelp restaurant reviews to check their versatility because they are not designed for one type of dataset but meant to be used for all sorts of reviews.

We have used two types of approaches:
1. Dictionary tools based approach using SentiWordNet 3.0
2. Dictionary tools based approach using TextBlob
3. CNNs
4. Neural Network


For Neural Networks and CNNs we use tfidf to vectorise the given sentences and use these as inputs to train the deep networks.

## Dictionary tools based approach
We have used an implementation where sentiment scores are between -1 and 1, more than 0 for positive reviews and less than 0 for negative reviews. We tried our own implementation but couldn't get nice results. The implementation handles negations. We have a SentiWordNet, a collection of words containg its POS, positive and negative score, different sense of words and choice of weighting across word senses based on Sentiment Analysis: How to Derive Prior Polarities from SentiWordNet by Marco Guerini. There are three types of weights:
1. Average
2. Geometric
3. Harmonic

Other than using weights from SentiWordNet, we also tried using weights from another tool called TextBlob giving almost similar results.

## Neural Network
We tried on CNNs using tfidf to vectorise the given sentence. We are using a two layer neural network having sigmoid as the normaliser and relu as the error function. 
## CNN
We also tried on CNNs again using tfidf to create vectors of review sentences. We used regularisation using dropout and loss function used is ReLu along with softmax to normalise. 

# 3. Opinosis
Third major part of our pipeline. We now have an aspect and a set of sentences describing the positive side of the aspect and another set describing its negatives. But this is not enough. Now there is too much data and redundancy. Hence all this summarized information might not be very useful to the user. Thus we introduce the idea of Opinosis in our model. We thus aim to generate concise summaries using the existing classified text that we have.


## Idea
The major focus of the Opinosis Summarization framework is to generate very short abstractive summaries when there is a large amount of text. The algorithm uses a word-graph data structure which is known as the Opinosis-Graph which represents the text which is to be summarized. We then continuously explore the Opinosis-Graph in depth first fashion to generate all the candidate summary phrases. The way that the algorithm works can generate phrases not seen before and hence it is not purely an extractive summarizer but a “shallow” abstractive summarizer.

## High Level Overview
1. Get topic specific and POS annotated text
2. Create the Opinosis graph from the text
3. Find all candidate paths(summaries) and score them

## Building the Graph
1. A unique tuple (word, POS tag) will make a unique node. Each node will contain a list of (sid, pid) tuple which donates the sentence id and position id of every occurence of the previously mentioned node.
2. An edge exists between two nodes a,b if (a,b) exist as a bigram in the text. 

## Generating candidate Summaries
1. A valid path is a set of connected nodes which have a valid start node, a valid end node and the entire path follows a well-formed order of POS tags.
2.  We then score all the valid paths based on path redundancy.
3.  Some nodes are collapsible, i.e could be broken down into anchor part and other valid paths. These nodes are collapsed and then stitched together using a proper coordinating conjunction to form a sentence. 

## Important Properties of the Opinosis Graph
1. Redundancy Capture: Naturally captures paths which are shared by multiple sentences. Those highly redundant paths tend to be the important shared opinion by a lot of reviews.
2. Gapped Subsequence Capture: Helps capture similar sentences with minor variations. For example the screen is very bright, and the screen is bright both capture the same idea that the screen of the phone is bright but the only difference is that in sentence 1, there is a gap of one word.
3. Collapsible Structures: Certain nodes are collapsible. For example in The iphone’s battery is heavy. And the iphone’s battery is long lasting. Here the node ‘is’ acts as a hub and can be used to generate squashed and compressed summaries like: the iphone’s battery is heavy but long lasting.

