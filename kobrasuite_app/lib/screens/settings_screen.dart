import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../main.dart';

class SettingsScreen extends StatelessWidget {
  const SettingsScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final themeNotifier = Provider.of<ThemeNotifier>(context);

    return Scaffold(
      appBar: AppBar(title: const Text('Settings')),
      body: ListView(
        children: [
          SwitchListTile(
            title: const Text('Dark Mode'),
            value: themeNotifier.isDarkMode,
            onChanged: (val) {
              themeNotifier.toggleTheme();
            },
          ),
          const Divider(),
          // Other settings
          ListTile(
            leading: const Icon(Icons.color_lens),
            title: const Text('Primary Color'),
            onTap: () {
              // Future color picking logic
            },
          ),
        ],
      ),
    );
  }
}