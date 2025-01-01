import 'package:flutter/material.dart';

class KobraDrawer extends StatelessWidget {
  final int selectedIndex;
  final ValueChanged<int> onItemTap;

  const KobraDrawer({
    Key? key,
    required this.selectedIndex,
    required this.onItemTap,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final navItems = [
      {'label': 'Dashboard', 'icon': Icons.dashboard},
      {'label': 'Finances', 'icon': Icons.account_balance_wallet},
      {'label': 'Homelife', 'icon': Icons.home},
      {'label': 'Investing', 'icon': Icons.trending_up},
      {'label': 'School', 'icon': Icons.school},
      {'label': 'Work', 'icon': Icons.work},
      {'label': 'Notifications', 'icon': Icons.notifications},
    ];

    return Drawer(
      child: SafeArea(
        child: Column(
          children: [
            const SizedBox(height: 16),
            // Placeholder user info or brand logo
            const CircleAvatar(
              radius: 40,
              backgroundImage: AssetImage('assets/images/profile_placeholder.png'),
            ),
            const SizedBox(height: 8),
            Text(
              'Welcome, User!',
              style: Theme.of(context).textTheme.titleMedium,
            ),
            const Divider(),
            Expanded(
              child: ListView.builder(
                itemCount: navItems.length,
                itemBuilder: (context, index) {
                  final item = navItems[index];
                  return ListTile(
                    leading: Icon(item['icon'] as IconData),
                    title: Text(item['label'] as String),
                    selected: (index == selectedIndex),
                    onTap: () {
                      onItemTap(index);
                      Navigator.pop(context); // closes Drawer
                    },
                  );
                },
              ),
            ),
            // Add the "Settings" item pinned at the bottom
            const Divider(),
            ListTile(
              leading: const Icon(Icons.settings),
              title: const Text('Settings'),
              onTap: () {
                // Indicate settings by using an invalid index, e.g. -1
                onItemTap(-1);
                Navigator.pop(context);
              },
            ),
            const SizedBox(height: 16),
          ],
        ),
      ),
    );
  }
}