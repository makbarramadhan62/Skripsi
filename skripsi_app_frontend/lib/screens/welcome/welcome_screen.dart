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
            width: size.width * 1.2,
            bottom: 120,
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
                          color: kBlackClr,
                        ),
                      ),
                      const SizedBox(
                        height: 10,
                      ),
                      const Icon(
                        Icons.circle,
                        size: 10,
                        color: kButtonClr,
                      ),
                      const SizedBox(
                        height: 10,
                      ),
                      const Text(
                        "Selamat Datang di",
                        style: TextStyle(
                          fontSize: 32,
                          fontWeight: FontWeight.bold,
                          color: kBlackClr,
                        ),
                      ),
                      Row(
                        children: [
                          const Text(
                            "Grapsense",
                            style: TextStyle(
                              color: kHighlightTxtClr,
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
                                color: kBetaClr,
                                width: 2,
                              ),
                            ),
                            child: const Center(
                              child: Text(
                                "Beta",
                                style: TextStyle(color: kBetaClr),
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
                            color: kSubTxtClr,
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
                      "Dengan mengklik Mulai, Anda menyetujui Syarat dan Ketentuan Penggunaan grapsense",
                      style: TextStyle(
                        color: kSubTxtClr,
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
                      backgroundColor: kButtonClr,
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
                      "Mulai",
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
