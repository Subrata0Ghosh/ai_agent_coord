const express = require('express');
const app = express();
app.use(express.json());

app.post('/task', (req, res) => {
  const task = req.body;
  console.log("Frontend Agent received:", task);
  const reactCode = `import React from 'react';\nexport default function Demo(){return <div>${task.description}</div>}`;
  res.json({ task_id: task.task_id, status: "done", files: [{ path: "src/components/Demo.jsx", content: reactCode }] });

});

app.listen(9001, () => console.log("Frontend Agent running on port 9001"));
