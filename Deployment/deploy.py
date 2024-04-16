from brownie import PawNFT, accounts, network, config
import subprocess

def calculate_score():
    code = """
    #include <iostream>
    #include <vector>
    #include <algorithm>
    #include <string>
    using namespace std;
    // Function to normalize a value within a given range
    double normalize(double value, double min, double max) {
        return (value - min) / (max - min);
    }
    // Function to calculate the score based on the values and their weights
    double calculateScore(vector<double>& values, vector<double>& weights) {
        double score = 0.0;

        // Minimum and maximum values for each variable
        vector<double> min_values = {0, 0, 0, 0, 0, 0, 14, 0, 0};
        vector<double> max_values = {1, 10, 200, 15, 150, 25, 100, 5, 5};
        
        // Calculate the score for the first 6 variables
        for (int i = 0; i < 6; ++i) {
            score += normalize(values[i], min_values[i], max_values[i]) * weights[i];
        }
        
        // Calculate the score for the 7th variable (closer to 28-59 is better)
        score += normalize(abs(values[6] - 59), 0, 43) * weights[6];
        
        // Calculate the score for the 8th variable (closer to 0-2 is better)
        score += normalize(abs(values[7] - 1), 0, 2) * weights[7];
        
        // Calculate the score for the 9th variable (smaller is better)
        score += (1 - normalize(values[8], min_values[8], max_values[8])) * weights[8];
        
        return score;
    }

    int main() {
        // Instructiions
        cout << "";
        
        // Weights for different species
        vector<double> weightsC = {0.3044, 0.1806, 0.1084, 0.0941, 0.0564, 0.0564, 0.0332, 0.0332, 0.1333};
        vector<double> weightsD = {0.2488, 0.1544, 0.1566, 0.0908, 0.0626, 0.0659, 0.0392, 0.0271, 0.1544};
        vector<double> weightsH = {0.3107, 0.1337, 0.1825, 0.0713, 0.0492, 0.0930, 0.0339, 0.0239, 0.1019};
        vector<double> weightsR = {0.2787, 0.2053, 0.1310, 0.0510, 0.0852, 0.0708, 0.0337, 0.0276, 0.1168};
        vector<double> weightsL = {0.2367, 0.2778, 0.1397, 0.1087, 0.0777, 0.0501, 0.0280, 0.0194, 0.0618};
        
        // Read the species from the input
        string spec;
        cin >> spec;
        
        // Select the weights based on the species
        vector<double> weights;
        
        if (spec == "CAT" || spec == "Cat") {
            weights = weightsC;
        } else if (spec == "DOG" || spec == "Dog") {
            weights = weightsD;
        } else if (spec == "RABBIT" || spec == "Rabbit") {
            weights = weightsR;
        } else if (spec == "HAMSTER" || spec == "Hamster") {
            weights = weightsH;
        } else if (spec == "LIZARD" || spec == "Lizard") {
            weights = weightsL;
        } else {
            cout << "The model for this species is still in progress :)";
            return 1;
        }
        
        // Read the values from the input
        vector<double> values(9);
        for (double& value : values) {
            cin >> value;
        }
        
        // Make sure the values is possible
        if (values[6] < 14) {
            cout << "Sorry, you're too young for getting a pet. Go get your parents' permission :)";
            return 1;
        }
        if (values[6] > 99) {
            cout << "Sorry, you're too old for getting a pet :)";
            return 1;
        }
        if (values[7] > 5) {
            cout << "Wow, you got already many kids to take care of! Good luck!";
        }
        if (values[8] > 5) {
            cout << "Wow, you got already many pets to take care of! Good luck!";
        }
        
        // Calculate and print the score
        double score = calculateScore(values, weights);
        
        int finalScore = score * 10000;
        // Write the score to the file
        cout << "Score: " << finalScore << endl;
        
        return 0;
    }
    """
    with open('score.cpp', 'w') as f:
        f.write(code)

    # Compile the C++ code
    subprocess.run(['g++', 'score.cpp', '-o', 'score'])

    # Run the compiled code and get the output
    output = subprocess.check_output(['./score'])
    return int(output.decode('utf-8').split(": ")[1].strip())

def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    publish_source = False
    contract = PawNFT.deploy({"from": dev}, publish_source=publish_source)

    score = calculate_score()
    contract.safeMint(dev, score, {"from": dev})
