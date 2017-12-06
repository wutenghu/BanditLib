# BanditLib
This repo contains the implementation of serveral contextual bandits algorithm, including CoLin, hLinUCB, factorUCB, GOB.Lin, LinUCB, HybridLinUCB, PTS, and UCBPMF. CoLin, hLinUCB and factorUCB are our proposed algorithms published in [1], [2], [3].

##Usage
Run the simulator: `python Simulation.py --alg XXX` where parameter alg represents the name of algorithm. 

Run with different parameters: `python Simulation.py --alg XXX --contextdim XX --userNum XX --Sparsity XX --NoiseScale XX --matrixNoise  XX --hiddendim XX` 
where 
`--contextdim` stands for dimension of contextual features;
`--userNum` stands for the number of users simulated in the simulator. Each user is associated with a preference parameter, which is known to the environment but not to the algorithms. In simulator, we can choose to simulate users every time we run the program or simulate users once, save it to 'Simulation_MAB_files', and keep using it.
`--Sparsity` stands for the sparsity level of the user graph. Sparsity XX means to only maintain the top XX most connected users. Sparsity should be smaller than userNum, when equal to userNum, the graph is a full connected graph'
`--hiddendim`stands for dimension of hidden features. This parameter is specifically for the algorithms that can estimate hidden features, such as hLinUCB, PTS. For all the other contextual bandit algorithms, the default setting for this parameter should be 0.

##Algorithms' details
**LinUCB**: A state-of-art contextual bandit algorithm. It select arms based on an `upper confidence bound (UCB)` of the estimated reward with given context vectors. LinUCB assume that users/bandits' parameters are independent with each other. And LinUCB only works with the observed features and does not consider hidden features.

**CoLin**: A collaborative contextual bandit algorithm which explicitly models the underlying dependency among users/bandits. In CoLin, a `weighted adjacency graph` is constructed, where each node represents a contextual bandit deployed for a single user and the weight on each edge indicates the influence between a pair of users. Based on this dependency structure, the observed payoffs on each user are assumed to be determined by a mixture of neighboring users in the graph. Bandit parameters over all the users are estimated in a collaborative manner: both context and received payoffs from one user are prorogated across the whole graph in the process of online updating. CoLin establishes a bridge to share information among heterogenous users and thus reduce the sample com- plexity of preference learning. We rigorously prove that our CoLin achieves a remarkable reduction of upper regret bound with high probability, comparing to the linear regret with respect to the number of users if one simply runs independent bandits on them (LinUCB). 

**hLinUCB**: A contextual bandit algorithm with hidden feature learning, in which hidden features are explicitly introduced in our reward generation assumption, in addition to the observable contextual features. Coordinate descent with provable exploration bound is used to iteratively estimate the hidden features and unknown model parameters on the fly. At each iteration, closed form solutions exist and can be efficiently computed. Most importantly, we rigorously prove that with proper initialization the developed hLinUCB algorithm with hidden features learning can obtain a sublinear upper regret bound with high probability, and a linear regret is inevitable at the worst case if one fails to model such hidden features.

**FactorUCB**: A factorization-based bandit algorithm, in which low-rank matrix completion is performed over an incrementally constructed user-item preference matrix and where an upper confidence bound based item selection strategy is developed to balance the exploit/explore trade-off in online learning. Observable conextual features and dependency among users (e.g., social influence) are leveraged to improve the algorithm’s convergence rate and help conquer cold-start in recommendation. A high probability sublinear upper regret bound is proved in the developed algorithm, where considerable regret reduction is achieved on both user and item sides.

##Result
The results will be written under folder `./SimulationResults`, including accumulated regret and parameter estimation error. You can then plot the result, and here are one example we used in [1], where we run the simulator to compare CoLin, GOB.Lin, LinUCB, and HybridLinUCB:

![image](SimulationResults/regret.png "regret")
![image](SimulationResults/ParameterEstimation.png "ParameterEstimation")
##Reference
[1]: Qingyun Wu, Huazheng Wang, Quanquan Gu and Hongning Wang. Contextual Bandits in A Collaborative Environment. The 39th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR'2016), p529-538, 2016.

[2]: Huazheng Wang, Qingyun Wu and Hongning Wang. Learning Hidden Features for Contextual Bandits. The 25th ACM International Conference on Information and Knowledge Management (CIKM 2016), p1633-1642, 2016.

[3]: Huazheng Wang, Qingyun Wu and Hongning Wang. Factorization Bandits for Interactive Recommendation. The Thirty-First AAAI Conference on Artificial Intelligence (AAAI 2017). (to appear)

