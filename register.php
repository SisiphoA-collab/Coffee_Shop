<?php
// Start the session
session_start();

// Include database connection
include 'db_connection.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST['username'];
    $password = password_hash($_POST['password'], PASSWORD_DEFAULT); // Hash the password for security

    // Insert into database
    $sql = "INSERT INTO users (username, password) VALUES ('$username', '$password')";

    if (mysqli_query($conn, $sql)) {
        $_SESSION['success'] = "Registration successful! You can now log in.";
        header("Location: login.php");
        exit();
    } else {
        $_SESSION['error'] = "Registration failed: " . mysqli_error($conn);
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>
    <h2>Register</h2>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" name="username" required><br>
        <label for="password">Password:</label>
        <input type="password" name="password" required><br>
        <button type="submit">Register</button>
    </form>
    <?php if (isset($_SESSION['error'])): ?>
        <p><?php echo $_SESSION['error']; unset($_SESSION['error']); ?></p>
    <?php endif; ?>
</body>
</html>
