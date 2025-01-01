import 'package:flutter/material.dart';

class KobraNavRail extends StatelessWidget {
  final int selectedIndex;
  final ValueChanged<int> onItemTap;

  const KobraNavRail({
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

    return NavigationRail(
      selectedIndex: selectedIndex,
      onDestinationSelected: onItemTap,
      labelType: NavigationRailLabelType.all,
      leading: const Padding(
        padding: EdgeInsets.all(8.0),
        child: FlutterLogo(size: 40),
      ),
      destinations: navItems.map((item) {
        return NavigationRailDestination(
          icon: Icon(item['icon'] as IconData),
          selectedIcon: Icon(
            item['icon'] as IconData,
            color: Theme.of(context).colorScheme.primary,
          ),
          label: Text(item['label'] as String),
        );
      }).toList(),
    );
  }
}