# PawGuard
A pet holder readiness evaluation model with NFT rewards and DAO oversight

<img width="759" alt="Screenshot 2024-04-18 at 11 53 23 PM" src="https://github.com/HuaEdward/PawChain/assets/102205131/d910433d-4a83-4b62-9ff0-00899fb5a6f1">

More analyzing models for pets: https://github.com/HuaEdward/analyzing-models-for-pets-1.0

# Instructions
In the 'MathModel' folder, the maths model built for evaluating the readiness of a person to become a qualified pet owner.

Input to the code as: the specie of the pet (`Cat`, `Dog`, `Rabbit`, `Hamster`, `Lizard`) + each value of the factors

<img width="1232" alt="Screenshot 2024-04-15 at 8 02 13 PM" src="https://github.com/HuaEdward/PawChain/assets/102205131/2820d570-8ce6-41d6-8aa2-c3f750924ec0">

Sample input: `Cat 1 9 30 8 25 8 55 1 0`


In the 'Contracts' foler, a smart contract is built to reward an NFT for the user who gets a score over 7000.

![未命名文件 (1)](https://github.com/HuaEdward/PawChain/assets/102205131/c042da08-cfea-42ee-b0e8-23348ee02553)

# Model Introduction
We use the Analytic Hierarchy Process (AHP) to determine the weight of each factor. 

- Model the problem as a hierarchy.
- Perform pairwise comparisons to establish priorities.
- Calculate the relative priority weights of the criteria.
- Synthesize the judgments to get overall priorities.
- Check for inconsistencies in the judgments.

![15181712019697_ pic](https://github.com/HuaEdward/PawChain/assets/102205131/ec2a5de7-b965-40b2-9862-13b8f602bfa6)


```
weightsC = {0.3044, 0.1806, 0.1084, 0.0941, 0.0564, 0.0564, 0.0332, 0.0332, 0.1333};
weightsD = {0.2488, 0.1544, 0.1566, 0.0908, 0.0626, 0.0659, 0.0392, 0.0271, 0.1544};
weightsH = {0.3107, 0.1337, 0.1825, 0.0713, 0.0492, 0.0930, 0.0339, 0.0239, 0.1019};
weightsR = {0.2787, 0.2053, 0.1310, 0.0510, 0.0852, 0.0708, 0.0337, 0.0276, 0.1168};
weightsL = {0.2367, 0.2778, 0.1397, 0.1087, 0.0777, 0.0501, 0.0280, 0.0194, 0.0618};
```

Then, we use Weighted Linear Combination (WLC).

Each criterion is assigned a weight that reflects its importance relative to the other criteria. The alternative with the highest total score is considered the best.



