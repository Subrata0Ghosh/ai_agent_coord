const express = require('express');
const app = express();
app.use(express.json());

app.post('/task', (req, res) => {
  const task = req.body;
  console.log("Frontend Agent received:", task);
  const filename = task.description.replace(/\s+/g, '_') + '.jsx';
  res.json({
    task_id: task.task_id,
    status: "done",
    files: [
      {
        path: `src/components/${filename}`,
        content: `import React from 'react';\nexport default function Demo(){return <div>${task.description}</div>}`
      }
    ]
  });
});

app.listen(9001, () => console.log("Frontend Agent running on port 9001"));
