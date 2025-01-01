import 'package:flutter/material.dart';

class SchoolScreen extends StatelessWidget {
  const SchoolScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Placeholder: courses, assignments, submissions
    return Scaffold(
      body: Column(
        children: [
          const SizedBox(height: 16),
          Text(
            'School Module',
            style: Theme.of(context).textTheme.headlineSmall,
          ),
          const Divider(),
          Expanded(
            child: ListView(
              padding: const EdgeInsets.all(16),
              children: [
                Card(
                  child: ListTile(
                    leading: const Icon(Icons.book),
                    title: const Text('Course: Intro to Math'),
                    subtitle: const Text('Assignments: 2 due'),
                  ),
                ),
                Card(
                  child: ListTile(
                    leading: const Icon(Icons.group),
                    title: const Text('Study Group: Algebra'),
                    subtitle: const Text('3 members'),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}