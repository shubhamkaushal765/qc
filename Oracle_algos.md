> folder: oracle_algos

# Deutsch's Algorithm

- An oracle function is used, and we have to determine the characteristics of this function. (constant or balanced)

$$
|x\rangle |-\rangle \rightarrow (-1)^{f(x)} |x\rangle |-\rangle
$$

- Phase kickback phenomenon is used.

![Deutsch Algorithm](https://www.researchgate.net/publication/342979428/figure/fig2/AS:913917110919170@1594906227180/The-Deutsch-Algorithm.jpg)

The lower qubit is initialized in the $|-\rangle$ state. The upper qubit is put in a superposition state. The oracle acts in it, phase kickback occurs and then we measure the input qubit to determine if the function f(x) is constant or balanced.

# Deutsch-Jozsa Algorithm

> Resources: [Classiq.io](https://www.classiq.io/insights/the-deutsch-jozsa-algorithm-explained), 

- Tells if a boolean function is balanced or constant.
- The oracle uses phase kickback to determine if the function is constant or balanced.

![Deutsch-Jozsa Algorithm](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Deutsch-Jozsa-algorithm-quantum-circuit.png/400px-Deutsch-Jozsa-algorithm-quantum-circuit.png)

