# Deutsch's Algorithm


- An oracle function is used, and we have to determine the characteristics of this function. (constant or balanced)

$$
|x\rangle |-\rangle \rightarrow (-1)^{f(x)} |x\rangle |-\rangle
$$

- Phase kickback phenomenon is used.

![image](https://www.researchgate.net/publication/342979428/figure/fig2/AS:913917110919170@1594906227180/The-Deutsch-Algorithm.jpg)

The lower qubit is initialized in the $|-\rangle$ state. The upper qubit is put in a superposition state. The oracle acts in it, phase kickback occurs and then we measure the input qubit to determine if the function f(x) is constant or balanced.