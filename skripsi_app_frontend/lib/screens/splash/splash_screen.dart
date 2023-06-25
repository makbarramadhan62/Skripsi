import 'package:flutter/material.dart';
import 'package:skripsi_app_frontend/screens/welcome/welcome_screen.dart';
import 'package:skripsi_app_frontend/utilities/colors.dart';

class SplashScreen extends StatefulWidget {
  const SplashScreen({super.key});

  @override
  State<SplashScreen> createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  @override
  void initState() {
    super.initState();
    Future.delayed(const Duration(seconds: 3), () {
      Navigator.pushAndRemoveUntil(
          context,
          MaterialPageRoute(
            builder: (context) => const WelcomeScreen(),
          ),
          (route) => false);
    });
  }

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Scaffold(
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(20),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Spacer(),
              Container(
                height: size.height * 0.25,
                decoration: const BoxDecoration(
                  image: DecorationImage(
                    image: AssetImage("assets/images/logo.png"),
                  ),
                ),
              ),
              const Spacer(),
              Container(
                height: size.height * 0.025,
                width: size.width * 0.25,
                decoration: BoxDecoration(
                  color: Colors.transparent,
                  borderRadius: BorderRadius.circular(10),
                  border: Border.all(
                    color: kBetaClr,
                    width: 2,
                  ),
                ),
                child: const Center(
                  child: Text(
                    "Beta Version",
                    style: TextStyle(color: kBetaClr),
                  ),
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
