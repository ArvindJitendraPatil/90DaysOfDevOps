<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Task 5 - Environment Variables</title>
  <style>
    body {
      font-family: 'Segoe UI', Arial, sans-serif;
      background: linear-gradient(135deg, #1f1c2c, #928dab);
      color: #f4f4f4;
      text-align: center;
      padding: 50px;
    }
    h1 {
      color: #ffcc00;
      text-shadow: 2px 2px 5px #000;
    }
    .env-box {
      background: rgba(255,255,255,0.1);
      border: 2px solid #ffcc00;
      border-radius: 12px;
      display: inline-block;
      padding: 25px;
      margin-top: 30px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.5);
    }
    .env-box p {
      margin: 12px 0;
      font-size: 18px;
      color: #00ffcc;
    }
    .env-box strong {
      color: #ffcc00;
    }
    .footer {
      margin-top: 40px;
      font-size: 14px;
      color: #ddd;
    }
  </style>
</head>
<body>
  <h1>🚀 Docker Compose – Task 5</h1>
  <p>This page shows environment variables injected into the container:</p>

  <div class="env-box">
    <p><strong>APP_ENV:</strong> <?php echo getenv("APP_ENV"); ?></p>
    <p><strong>DB_HOST:</strong> <?php echo getenv("DB_HOST"); ?></p>
    <p><strong>MYSQL_DATABASE:</strong> <?php echo getenv("MYSQL_DATABASE"); ?></p>
  </div>

  <div class="footer">
    <p>Made with ❤️ by Arvind for 90DaysOfDevOps</p>
  </div>
</body>
</html>

