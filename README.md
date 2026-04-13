# 🚀 Serverless URL Shortener (AWS)

## 📌 Overview

A fully serverless URL shortener built on AWS. Users can submit a long URL and receive a short link, which redirects to the original destination when accessed. The entire system is designed using scalable, event-driven architecture with zero server management.

---

## 🔗 Live Demo

👉 https://YOUR-CLOUDFRONT-URL.cloudfront.net

---

## 🏗️ Architecture

Frontend is hosted on S3 and delivered via CloudFront. API Gateway handles HTTP requests and triggers AWS Lambda. Lambda processes requests and stores/retrieves data from DynamoDB.



---

## ☁️ AWS Services Used

* **AWS Lambda**
  Executes backend logic without managing servers.

* **Amazon DynamoDB**
  Stores shortCode → longUrl mappings with fast performance.

* **API Gateway**
  Exposes REST endpoints for creating and accessing short URLs.

* **Amazon S3**
  Hosts the frontend static website.

* **Amazon CloudFront**
  Delivers the frontend globally with low latency and HTTPS.

* **AWS IAM**
  Manages permissions securely between services.

* **AWS CDK**
  Infrastructure as Code for deploying resources in one command.

---

## ⚙️ How to Deploy

```bash
cd cdk-project
cdk deploy
```

---

## 💰 Cost Analysis

This project runs within AWS Free Tier:

* Lambda: Free for low requests
* DynamoDB: On-demand, minimal usage
* API Gateway: Free tier sufficient
* S3 + CloudFront: negligible cost for small traffic

👉 Estimated cost: **$0/month**

---

## 📚 What I Learned

* Building scalable serverless applications using AWS
* Designing REST APIs with API Gateway and Lambda
* Using DynamoDB for high-performance NoSQL storage
* Hosting static websites with S3 and CloudFront
* Implementing Infrastructure as Code using AWS CDK
* Setting up CI/CD with GitHub Actions

---

## 🚀 Future Improvements

* Add user authentication (AWS Cognito)
* Track click analytics for each short URL
* Custom domain integration
* Rate limiting and security enhancements

---
