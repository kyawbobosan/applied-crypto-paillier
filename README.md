# Paillier Homomorphic Encryption Implementation
**MSc Cybersecurity | Edinburgh Napier University**

## 🛡️ Project Overview
This repository demonstrates a practical implementation of the **Paillier Cryptosystem**, a probabilistic asymmetric algorithm for public-key cryptography. This project explores the unique **additive homomorphic properties** of Paillier, allowing mathematical operations to be performed on ciphertext without decryption.

## 🚀 Key Features
* **Asymmetric Key Generation**: Secure generation of public and private keypairs.
* **Homomorphic Addition**: Demonstrates $E(m_1 + m_2) = E(m_1) \cdot E(m_2) \pmod{n^2}$.
* **Scalar Multiplication**: Demonstrates multiplication of encrypted values by unencrypted constants.
* **Secure Decryption**: Verification of mathematical results post-decryption.

## 💻 Tech Stack
* **Language**: Python 3.12
* **Libraries**: `phe` (Partially Homomorphic Encryption)
* **Environment**: Virtual Environment (venv) for dependency isolation.

## 🛠️ Installation & Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/kyawbobosan/applied-crypto-paillier.git](https://github.com/kyawbobosan/applied-crypto-paillier.git)
   cd applied-crypto-paillier