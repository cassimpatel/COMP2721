# Algorithms & Data Structures II (COMP2721)
This repository contains a collection of implementations of algorithms and abstract data types, along with their respective methods

## Dynamic Programming
Dynamic programming solves problems using a bottom-up approach: solving smaller instances of the problem and using their solutions to build up to the solution of the larger problem.
 - [x] Matrix Chain Product
 - [x] Shortest paths in negatively weighted graphs
     - [x] Matrix multiplication
     - [x] Floyd Warshall Algorithm
 - [x] Cocke-Younger-Kasami (CYK) Algorithm
     - [ ] Generating parse trees from result
 - [ ] Travelling Salesperson

## Divide & Conquer
Divide & Conquer algorithms: solve an instance of a problem by breaking it into smaller instances until they have arbitrary solutions, then combining solutions to those smaller instances to construct the solution for the original instance.
- [ ] Minimum Independent Set (Multiple variants)
- [ ] Karatsuba's algorithm
- [ ] Strassen's algorithm: Matrix Multiplication

## Priority Queues
Priority queues offer access to a set of items ordered by a key. There are two possible implementations: binary heaps, and binomial heaps, both of which offer logarithmic times for operations.
- [x] Binary Heaps
- [ ] Binomial Heaps

## Dictionaries
Dictionaries offer random access to a set of key-value pairs, where keys must be unique. This includes implementations using two possible data structures: hash tables, and balanced search trees.
- [x] Hash Tables
	- [x] Linear Probing
	- [x] Quadratic Probing
	- [x] Double Hashing
	- [x] Double Hashing: Brent's improvement
 - [ ] Search Trees
    - [x] Natural Search Trees
    - [ ] Red-black Trees
    - [ ] AVL Trees
