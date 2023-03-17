import 'package:flutter/material.dart';
import 'package:skripsi_app_frontend/screens/home/home_screen.dart';
import 'package:skripsi_app_frontend/utilities/colors.dart';

class WelcomeScreen extends StatelessWidget {
  const WelcomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Scaffold(
      body: Stack(
        children: [
          Positioned(
            width: size.width * 1.15,
            bottom: 110,
            left: 75,
            child: Image.asset('assets/images/gambar_daun_up.png'),
          ),
          SafeArea(
            child: Padding(
              padding: const EdgeInsets.all(20),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  SizedBox(
                    height: size.height * 0.02,
                  ),
                  Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Text(
                        "marmdhn",
                        style: TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.w500,
                          color: KBlackClr,
                        ),
                      ),
                      const SizedBox(
                        height: 10,
                      ),
                      const Icon(
                        Icons.circle,
                        size: 10,
                        color: KButtonClr,
                      ),
                      const SizedBox(
                        height: 10,
                      ),
                      const Text(
                        "Welcome to",
                        style: TextStyle(
                          fontSize: 32,
                          fontWeight: FontWeight.bold,
                          color: KBlackClr,
                        ),
                      ),
                      Row(
                        children: [
                          const Text(
                            "Grapsense",
                            style: TextStyle(
                              color: KHighlightTxtClr,
                              fontSize: 32,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                          const SizedBox(
                            width: 5,
                          ),
                          Container(
                            height: size.height * 0.025,
                            width: size.width * 0.15,
                            decoration: BoxDecoration(
                              color: Colors.transparent,
                              borderRadius: BorderRadius.circular(10),
                              border: Border.all(
                                color: KBetaClr,
                                width: 2,
                              ),
                            ),
                            child: const Center(
                              child: Text(
                                "Beta",
                                style: TextStyle(color: KBetaClr),
                              ),
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(
                        height: 10,
                      ),
                      const Padding(
                        padding: EdgeInsets.only(right: 10),
                        child: Text(
                          "Deteksi cepat penyakit anggur Anda berdasarkan warna daunnya dengan Grapesense!",
                          style: TextStyle(
                            color: KSubTxtClr,
                            fontSize: 12,
                            fontWeight: FontWeight.w500,
                          ),
                        ),
                      ),
                    ],
                  ),
                  const Spacer(),
                  const Center(
                    child: Text(
                      "By clicking on Get Started, you agree to grapsense`s Terms and Conditions of Use",
                      style: TextStyle(
                        color: KSubTxtClr,
                        fontSize: 12,
                        fontWeight: FontWeight.w500,
                      ),
                      textAlign: TextAlign.center,
                    ),
                  ),
                  const SizedBox(
                    height: 10,
                  ),
                  ElevatedButton(
                    onPressed: () {
                      Navigator.pushAndRemoveUntil(
                          context,
                          MaterialPageRoute(
                            builder: (context) => const HomeScreen(),
                          ),
                          (route) => false);
                    },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: KButtonClr,
                      minimumSize: Size(size.width, 50),
                      shadowColor: Colors.grey,
                      elevation: 5,
                      shape: const RoundedRectangleBorder(
                        borderRadius: BorderRadius.all(
                          Radius.circular(20),
                        ),
                      ),
                    ),
                    child: const Text(
                      "Get Started",
                      style: TextStyle(
                        fontSize: 16,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  )
                ],
              ),
            ),
          )
        ],
      ),
    );
  }
}
