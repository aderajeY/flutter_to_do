// ignore_for_file: prefer_const_constructors

import 'package:flutter/material.dart';

class MyApp extends StatelessWidget{
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('To-Do app')),
      body: Container(
        child: Text('this is home page'),
      ),
    );
  }
}