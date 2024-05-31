import 'dart:async';

import 'package:flutter/material.dart';

void main() => runApp(const StreamBuilderExampleApp());

class StreamBuilderExample extends StatefulWidget {
  const StreamBuilderExample({super.key});

  @override
  State<StreamBuilderExample> createState() => _StreamBuilderExampleState();
}

class StreamBuilderExampleApp extends StatelessWidget {
  const StreamBuilderExampleApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: StreamBuilderExample(),
    );
  }
}

class _StreamBuilderExampleState extends State<StreamBuilderExample> {
  final Stream<int> _bids = (() {
    late final StreamController<int> controller;
    controller = StreamController<int>.broadcast(onListen: () async {
      int bid = 0;
      Timer.periodic(const Duration(seconds: 1), (_) async {
        await Future<void>.delayed(const Duration(seconds: 1));
        controller.add(bid);
        bid += 1;
      });
    });
    return controller.stream;
  })();

  @override
  Widget build(BuildContext context) {
    return DefaultTextStyle(
      style: Theme.of(context).textTheme.displayMedium!,
      textAlign: TextAlign.center,
      child: Container(
        alignment: FractionalOffset.center,
        color: Colors.white,
        child: StreamBuilder<int>(
          stream: _bids,
          builder: (context, snapshot) {
            if (snapshot.hasData) {
              return Text('Value: ${snapshot.data}');
            } else {
              return const CircularProgressIndicator();
            }
          },
        ),
      ),
    );
  }

  @override
  void initState() {
    super.initState();
    _bids.listen(
      (data) {
        print('Data received: $data');
      },
      onError: (error) {
        print('Error: $error');
      },
    );
  }
}
