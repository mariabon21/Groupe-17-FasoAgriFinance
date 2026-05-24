# Groupe-17-FasoAgriFinance
FasoAgriFinance is# 🌾 Project: FasoAgriFinance (v1.0)


## 📝 Project Description
FasoAgriFinance is a Python Command-Line Interface (CLI) application designed to modernize and secure financial management for agricultural cooperatives in Burkina Faso. 



📝 What the program does
FasoAgriFinance registers an agricultural producer, validates every input, and generates a financial summary report including:

A membership fee (with 25% discount for cooperative members)
An estimated harvest revenue based on yield and market price
Simple interest earned on savings over a chosen period
A net financial projection

 Classes
Person — parent class
Stores the identity shared by all members: last name, first name, age, phone number.
FarmerAccount(Person) — child class
A farmer account IS A person. Inherits identity from Person and adds:
AttributeTypeDescriptionfarm_sizefloatSize of the farm in hectarescropstrMain crop typesavingsfloatCurrent savings in FCFAis_coop_memberboolCooperative membership status
MethodDescriptionmembership_fee()Arithmetic 1 — base fee with optional 25% discountharvest_revenue()Arithmetic 2 — farm size × yield × pricesavings_interest()Arithmetic 3 — simple interest on savingsaccount_count()@classmethod — total accounts registered__str__()Magic method — controls print(account) output

🔬 Concepts researched
__str__ — magic dunder method
Python calls this automatically when print() is used on an object.
Without it Python displays: <FarmerAccount object at 0x...>
@classmethod — decorator
Receives the class itself (cls) as first argument instead of an instance.
Used here to read total_accounts, a variable shared across all instances.

 How to Run the Program
Step 1 — Make sure Python is installed
bashpython3 --version
You need Python 3.8 or higher.
Step 2 — Download the file
Download validator.py from this repository.
Step 3 — Run the program
bashpython validator.py


## 👥 Team Members & Project Contributions

| Full Name | Student Role | Core Technical Contribution |
| :--- | :--- | :--- |
| **[BONKOUNGOU Vanessa]** | **Git Master & Documentation** | Created the repository, managed commits, wrote the README |
| **[SIMPORE Alima]** | **Core OOP Developer** |Built the Person and FarmerAccount inheritance hierarchy |
| **[KABORE Albertine]** | **Security & Validation** | Built the validation functions with while + try/except. |
| **[GARANE Farida]** | **Financial Logic Engineer** | Designed the 3 arithmetic methods (fee, revenue, interest) |
| **[TAO Fazollah ]** | **Research & Optimization** | Integrated __str__ magic method and @classmethod decorator |

---

