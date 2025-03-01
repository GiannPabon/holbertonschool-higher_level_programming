# Task 0: HTTP/HTTPS Basics

## Differences between HTTP and HTTPS
- **HTTP (Hypertext Transfer Protocol)**  
  - Data is sent in plain text.  
  - Default port: 80.  
  - Vulnerable to eavesdropping and man-in-the-middle attacks.

- **HTTPS (HTTP Secure)**  
  - Data is encrypted with SSL/TLS.  
  - Default port: 443.  
  - Protects confidentiality and integrity of the data.

## Structure of an HTTP Request
1. **Request Line**: Method (GET, POST, etc.), Path (e.g., `/` or `/api`), HTTP version.  
2. **Headers**: Key/value pairs with metadata (Content-Type, Authorization, etc.).  
3. **Body** (optional): Data sent with methods like POST or PUT.

## Structure of an HTTP Response
1. **Status Line**: HTTP version, status code (e.g., `HTTP/1.1 200 OK`).  
2. **Headers**: Metadata about the server, content type, etc.  
3. **Body** (optional): The content returned by the server (HTML, JSON, etc.).

## Common HTTP Methods
- **GET**: Retrieve data from a resource.  
- **POST**: Create a new resource.  
- **PUT**: Update an existing resource (replaces entire resource).  
- **DELETE**: Remove a resource.  
- **PATCH**: Partially update an existing resource.

## Common HTTP Status Codes
- **200 OK**: The request was successful.  
- **201 Created**: A resource has been successfully created.  
- **400 Bad Request**: Malformed request syntax or invalid data.  
- **401 Unauthorized**: Missing or invalid credentials.  
- **404 Not Found**: The requested resource does not exist on the server.  
- **500 Internal Server Error**: A generic server error occurred.
