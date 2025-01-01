import 'package:flutter/material.dart';
import '../components/kobra_appbar.dart';
import '../components/kobra_drawer.dart';
import '../components/kobra_nav_rail.dart';
import 'finances_screen.dart';
import 'homelife_screen.dart';
import 'investing_screen.dart';
import 'school_screen.dart';
import 'work_screen.dart';
import 'notifications_screen.dart';
import 'home_dashboard_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  // The index of the current module selected
  int _selectedIndex = 0;

  // Simple array of screens for demonstration
  // index 0 => Dashboard, index 1 => Finances, etc.
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

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (ctx, constraints) {
        final bool isLargeScreen = constraints.maxWidth >= 800;

        return Scaffold(
          drawer: isLargeScreen
              ? null
              : KobraDrawer(
            selectedIndex: _selectedIndex,
            onItemTap: (index) {
              setState(() {
                _selectedIndex = index;
              });
            },
          ),
          body: Row(
            children: [
              // If large screen, show nav rail
              if (isLargeScreen)
                KobraNavRail(
                  selectedIndex: _selectedIndex,
                  onItemTap: (index) {
                    setState(() => _selectedIndex = index);
                  },
                ),
              // Main content
              Expanded(
                child: _screens[_selectedIndex],
              ),
            ],
          ),
        );
      },
    );
  }
}