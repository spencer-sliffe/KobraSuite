import 'package:flutter/material.dart';

import '../components/kobra_drawer.dart';
import '../components/kobra_nav_rail.dart';

import 'finances_screen.dart';
import 'homelife_screen.dart';
import 'investing_screen.dart';
import 'school_screen.dart';
import 'work_screen.dart';
import 'notifications_screen.dart';
import 'home_dashboard_screen.dart';
import 'account_screen.dart';
import 'settings_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  // The index of the current module selected
  int _selectedIndex = 0;

  // index 0 => Dashboard, 1 => Finances, 2 => Homelife, etc.
  late final List<Widget> _screens;

  @override
  void initState() {
    super.initState();
    _screens = [
      HomeDashboardScreen(onModuleSelected: _onModuleSelected),
      const FinancesScreen(),
      const HomelifeScreen(),
      const InvestingScreen(),
      const SchoolScreen(),
      const WorkScreen(),
      const NotificationsScreen(),
    ];
  }

  void _onModuleSelected(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  // Goes to account screen
  void _goToAccountScreen() {
    Navigator.push(
      context,
      MaterialPageRoute(builder: (_) => const AccountScreen()),
    );
  }

  // Goes to settings screen
  void _goToSettingsScreen() {
    Navigator.push(
      context,
      MaterialPageRoute(builder: (_) => const SettingsScreen()),
    );
  }

  @override
  Widget build(BuildContext context) {
    final bool isLargeScreen = MediaQuery.of(context).size.width >= 800;

    return Scaffold(
      appBar: AppBar(
        // top-left: Flutter logo + "Kobra Suite"
        title: Row(
          children: [
            // The Flutter logo at the far left
            const Padding(
              padding: EdgeInsets.only(right: 8.0),
              child: FlutterLogo(size: 30),
            ),
            const Text('Kobra Suite'),
          ],
        ),
        // top-right: only account button now, removed the settings button
        actions: [
          IconButton(
            icon: const Icon(Icons.account_circle),
            onPressed: _goToAccountScreen,
          ),
        ],
      ),

      // For small screens, use the Drawer
      drawer: isLargeScreen
          ? null
          : KobraDrawer(
        selectedIndex: _selectedIndex,
        onItemTap: (index) {
          if (index == -1) {
            // user tapped Settings in the Drawer
            _goToSettingsScreen();
          } else {
            setState(() => _selectedIndex = index);
          }
        },
      ),

      body: Row(
        children: [
          // Large screens: show side nav
          if (isLargeScreen)
          // We'll nest the NavigationRail + a bottom Settings icon in a Column
            Container(
              width: 72, // or 80, up to you
              color: Theme.of(context).colorScheme.surface,
              child: Column(
                children: [
                  // The main nav items (Dashboard, Finances, etc.)
                  Expanded(
                    child: KobraNavRail(
                      selectedIndex: _selectedIndex,
                      onItemTap: (index) {
                        setState(() => _selectedIndex = index);
                      },
                    ),
                  ),
                  // The bottom settings icon
                  IconButton(
                    icon: const Icon(Icons.settings),
                    onPressed: _goToSettingsScreen,
                  ),
                  const SizedBox(height: 16),
                ],
              ),
            ),

          // Main content area
          Expanded(
            child: _screens[_selectedIndex],
          ),
        ],
      ),
    );
  }
}