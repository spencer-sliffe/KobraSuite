import 'dart:convert';
import 'package:http/http.dart' as http;

class AuthService {
  // Replace with your actual backend base URL
  static const String baseUrl = 'https://kobrasuite-backend.azurewebsites.net';

  // A place to store the session cookie in memory
  static String? sessionCookie;

  /// Register a new user.
  ///
  /// [username], [email], [phoneNumber], [password], [confirmPassword]
  /// are the fields expected by your Django serializer.
  static Future<Map<String, dynamic>> register({
    required String username,
    required String email,
    required String phoneNumber,
    required String password,
    required String confirmPassword,
  }) async {
    final url = Uri.parse('$baseUrl/api/auth/register/');
    final response = await http.post(
      url,
      headers: {
        'Content-Type': 'application/json',
        // If your Django requires CSRF token, you need to add it here
        // 'X-CSRFToken': '<your-csrf-token>',
      },
      body: jsonEncode({
        'username': username,
        'email': email,
        'phone_number': phoneNumber,
        'password': password,
        'confirm_password': confirmPassword,
      }),
    );

    final data = jsonDecode(response.body);

    if (response.statusCode == 201) {
      // Registration successful
      return {
        'success': true,
        'message': data['message'] ?? 'Registered successfully',
      };
    } else {
      // Registration failed
      return {
        'success': false,
        'errors': data,
      };
    }
  }

  /// Log in an existing user.
  ///
  /// On success, store the session cookie from the response headers
  /// so future requests stay authenticated.
  static Future<Map<String, dynamic>> login({
    required String username,
    required String password,
  }) async {
    final url = Uri.parse('$baseUrl/api/auth/login/');
    final response = await http.post(
      url,
      headers: {
        'Content-Type': 'application/json',
      },
      body: jsonEncode({
        'username': username,
        'password': password,
      }),
    );

    final data = jsonDecode(response.body);

    if (response.statusCode == 200) {
      // Extract the session cookie from the response headers
      final cookies = response.headers['set-cookie'];
      if (cookies != null) {
        // Typically, Django sets a cookie like "sessionid=abc123; Path=/; HttpOnly"
        // We need to extract just "sessionid=abc123"
        // A quick approach:
        final cookie = cookies.split(';')[0];
        sessionCookie = cookie;
        // OPTIONAL: store in SharedPreferences or flutter_secure_storage for persistence
      }

      return {
        'success': true,
        'message': data['message'] ?? 'Logged in successfully',
      };
    } else {
      // Login failed
      return {
        'success': false,
        'errors': data,
      };
    }
  }

  static Future<Map<String, dynamic>> logout() async {
    final url = Uri.parse('$baseUrl/api/auth/logout/');
    final response = await http.post(
      url,
      headers: {
        'Content-Type': 'application/json',
        if (sessionCookie != null) 'Cookie': sessionCookie!,
      },
    );

    sessionCookie = null;

    if (response.statusCode == 200) {
      return {
        'success': true,
        'message': 'Logged out successfully',
      };
    } else {
      return {
        'success': false,
        'errors': jsonDecode(response.body),
      };
    }
  }
}