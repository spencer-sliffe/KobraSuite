import 'package:flutter/material.dart';

class InvestingScreen extends StatelessWidget {
  const InvestingScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Placeholder: portfolio, watchlist, etc.
    return Scaffold(
      body: Column(
        children: [
          const SizedBox(height: 16),
          Text(
            'Investing Module',
            style: Theme.of(context).textTheme.headlineSmall,
          ),
          const Divider(),
          Expanded(
            child: ListView(
              padding: const EdgeInsets.all(16),
              children: [
                Card(
                  child: ListTile(
                    leading: const Icon(Icons.trending_up),
                    title: const Text('Portfolio #1'),
                    subtitle: const Text('Total Value: \$15,230.00'),
                  ),
                ),
                Card(
                  child: ListTile(
                    leading: const Icon(Icons.remove_red_eye),
                    title: const Text('Watchlist'),
                    subtitle: const Text('AAPL, TSLA, BTC'),
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