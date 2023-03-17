import 'package:flutter/material.dart';
import 'package:skripsi_app_frontend/utilities/colors.dart';

class Button extends StatelessWidget {
  final VoidCallback press;
  final String text;

  const Button({
    super.key,
    required this.press,
    required this.text,
  });

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: press,
      style: ElevatedButton.styleFrom(
        backgroundColor: KButtonClr,
        minimumSize: const Size(165, 40),
        shadowColor: Colors.grey,
        elevation: 5,
        shape: const RoundedRectangleBorder(
          borderRadius: BorderRadius.all(
            Radius.circular(15),
          ),
        ),
      ),
      child: Text(
        text,
        style: const TextStyle(
          fontSize: 14,
          fontWeight: FontWeight.bold,
        ),
      ),
    );
  }
}
