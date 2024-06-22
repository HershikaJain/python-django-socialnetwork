1. System Architecture
Microservices:
1. User Service: Handles user registration, login, and profile management.
2. Discussion Service: Manages posts, hashtags, and image uploads.
3. Interaction Service: Handles likes, comments, and replies.
Additional Components:
- API Gateway: Routes requests to appropriate services.
- Auth Service: Manages authentication and authorization using JWT.
2. Low-Level Design (LLD)
a. User Service
Endpoints:
- POST /users/signup: Create a new user
- POST /users/login: Authenticate user and issue token
- GET /users/:id: Get user details
- PUT /users/:id: Update user information
- DELETE /users/:id: Delete a user
- GET /users/search: Search users by name
Database Schema (MongoDB):
{
 "_id": "ObjectId",
 "name": "string",
 "mobileNo": "string",

 "email": "string",
 "password": "string",
 "followers": ["ObjectId"],
 "following": ["ObjectId"]
}
b. Discussion Service
Endpoints:
- POST /discussions: Create a new discussion
- GET /discussions: List discussions (filter by tags or text)
- GET /discussions/:id: Get discussion details
- PUT /discussions/:id: Update discussion
- DELETE /discussions/:id: Delete discussion
Database Schema (MongoDB):
{
 "_id": "ObjectId",
 "userId": "ObjectId",
 "text": "string",
 "image": "string",
 "hashtags": ["string"],
 "createdOn": "date",
 "viewCount": "number"
}

c. Interaction Service
Endpoints:
- POST /discussions/:id/comments: Add comment
- PUT /comments/:id: Update comment
- DELETE /comments/:id: Delete comment
- POST /discussions/:id/like: Like a discussion
- POST /comments/:id/like: Like a comment
Database Schema (MongoDB):
{
 "_id": "ObjectId",
 "discussionId": "ObjectId",
 "userId": "ObjectId",
 "commentText": "string",
 "likes": ["ObjectId"],
 "createdOn": "date"
}
3. Database Schema Design
Users Collection:
{
 "_id": "ObjectId",
 "name": "string",
 "mobileNo": "string (unique)",
 "email": "string (unique)",

 "password": "string",
 "followers": ["ObjectId"],
 "following": ["ObjectId"]
}
Discussions Collection:
{
 "_id": "ObjectId",
 "userId": "ObjectId",
 "text": "string",
 "image": "string",
 "hashtags": ["string"],
 "createdOn": "date",
 "viewCount": "number"
}
Comments Collection:
{
 "_id": "ObjectId",
 "discussionId": "ObjectId",
 "userId": "ObjectId",
 "commentText": "string",
 "likes": ["ObjectId"],
 "createdOn": "date"
}

4. API Documentation
Create User
Endpoint: POST /users/signup
Request:
{
 "name": "John Doe",
 "mobileNo": "1234567890",
 "email": "jhershika29@example.com",
 "password": "password123"
}
Response:
{
 "message": "User created successfully",
 "userId": "ObjectId"
}
Create Discussion
Endpoint: POST /discussions
Request:
{
 "userId": "ObjectId",
 "text": "This is a discussion",
 "image": "image_url",
 "hashtags": ["#example", "#discussion"]
}

Response:
{
 "message": "Discussion created successfully",
 "discussionId": "ObjectId"
}
5. Deployment and Submission
- Deploy the microservices using Docker and Kubernetes.
- Push the code to a GitHub repository.
- Create a Postman collection for API testing and share the public link.
