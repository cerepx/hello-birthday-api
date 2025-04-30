## 📸 Live Demo Screenshots

Demonstrating the behavior of the Hello Birthday API with real request/response examples.

---

### ✅ PUT `/hello/{username}` – Valid Request

Creates or updates a user's date of birth.

<img src="assets/put-user-success.png" alt="PUT user success" width="600"/>

---

### ❌ PUT `/hello/{username}` – Invalid Date Format

User submitted a date in an incorrect format.

<img src="assets/put-user-invalid-date.png" alt="PUT user invalid date" width="600"/>

---

### ✅ GET `/hello/{username}` – Birthday Check Success

Returns a birthday greeting or countdown.

<img src="assets/get-user-success.png" alt="GET user success" width="600"/>

---

### ❌ GET `/hello/{username}` – User Not Found

The requested user is not yet registered.

<img src="assets/get-user-not-found.png" alt="GET user not found" width="600"/>

---

### ❌ GET `/hello/{username}` – Invalid Username

Invalid URL, missing params, etc.

<img src="assets/get-user-invalid-username.png" alt="GET user error" width="600"/>
