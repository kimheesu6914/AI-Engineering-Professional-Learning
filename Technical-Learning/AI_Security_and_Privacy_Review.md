# Goal 2: Foundational Cybersecurity Skills in an AI Context

As an aspiring AI Engineer, I recognise that cybersecurity is not just an infrastructure concern, but a core software engineering practice. This review documents my foundational learning of security principles applied to AI pipelines.

## The CIA Triad in AI Data Workflows
I have analyzed how the core security goals (Confidentiality, Integrity, and Availability) apply directly to the data processing workflow I established in **Goal 4**:

* **Confidentiality**: Training datasets often contain sensitive user interactions or proprietary information. As a professional developer, I must ensure that data access is restricted to authorized environments and that user logs are anonymized during the preprocessing stage to protect privacy.
* **Integrity**: Data poisoning is a major threat to machine learning models. If a malicious actor tampers with training data or labels, the model's accuracy degrades. The preprocessing and input validation scripts I created in Goal 4 (`.isnull().sum()` and duplicate checks) serve as a baseline to maintain data integrity and prevent corrupted inputs from affecting the model.
* **Availability**: For a Conversational AI system, ensuring that the model's inference API is resilient against service disruptions (such as DoS attacks) is critical to maintaining continuous user interactions.

## Secure Coding & Risk Assessment Reflection
Through the introductory cybersecurity learning materials, I have shifted my mindset toward proactive risk management:
1. **Input Validation**: I learned that raw user inputs are a primary attack vector. Stripping whitespace and replacing empty strings are not just for formatting accuracy, but also clear out anomalies that could lead to basic injection vulnerabilities.
2. **Traceability**: Documenting every data transformation ensures that if a security anomaly or data drift occurs, the engineering team can trace the pipeline back to its root cause, establishing technical accountability.

## Professional Growth
Understanding cybersecurity fundamentals has made me realize that building safe software is just as important as building accurate AI models. In my future career as an AI Engineer, I will prioritize data privacy and secure code practices from the earliest stages of development.
