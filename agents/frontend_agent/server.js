const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();
app.use(express.json());

// Generate React component from description
function generateReactCode(description) {
  if (description.toLowerCase().includes("login")) {
    return `
import React, { useState } from 'react';

export default function Login() {
  const [user, setUser] = useState('');
  const [pass, setPass] = useState('');
  const handleLogin = () => alert(\`Welcome \${user}!\`);

  return (
    <div style={{margin:'50px'}}>
      <h2>Login</h2>
      <input placeholder="User ID" onChange={e => setUser(e.target.value)} />
      <input type="password" placeholder="Password" onChange={e => setPass(e.target.value)} />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
}`;
  }

  // Default fallback
  return `
import React from 'react';
export default function Demo(){return <div>${description}</div>}
`;
}

app.post('/task', (req, res) => {
  const { task_id, project, description } = req.body;
  console.log("Frontend Agent received:", description);

  // Generate React code dynamically
  const code = generateReactCode(description);

  // Define file path
  const filePath = path.join("src", "components", `${description.replace(/\s+/g, '_')}.jsx`);

  // Return JSON (Coordinator will save it)
  res.json({
    task_id,
    status: "done",
    files: [{ path: filePath, content: code }]
  });
});

app.listen(9001, () => console.log("✅ Frontend Agent running on port 9001"));
