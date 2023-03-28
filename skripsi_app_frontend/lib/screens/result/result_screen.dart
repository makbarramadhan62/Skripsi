import 'package:flutter/material.dart';
import 'package:skripsi_app_frontend/screens/home/home_screen.dart';
import 'package:skripsi_app_frontend/screens/result/models/list_data.dart';

import '../../utilities/colors.dart';

class ResultScreen extends StatefulWidget {
  final DataInfo dataInfo;
  const ResultScreen({super.key, required this.dataInfo});

  @override
  State<ResultScreen> createState() => _ResultScreenState();
}

class _ResultScreenState extends State<ResultScreen> {
  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: const Text(
          "Classification Results",
          style: TextStyle(
            fontSize: 20,
            fontWeight: FontWeight.bold,
            color: KButtonClr,
          ),
        ),
        backgroundColor: Colors.transparent,
        elevation: 0,
      ),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.symmetric(
            horizontal: 30,
            vertical: 20,
          ),
          child: Center(
            child: Column(
              children: [
                Column(
                  children: [
                    Image.asset(
                      "assets/images/gambar_daun_down.png",
                      width: size.width * 0.75,
                    ),
                    SizedBox(
                      height: size.height * 0.05,
                    ),
                    Text(
                      widget.dataInfo.name,
                      style: const TextStyle(
                        fontSize: 24,
                        fontWeight: FontWeight.w800,
                        color: KBlackClr,
                      ),
                    ),
                    SizedBox(
                      height: size.height * 0.025,
                    ),
                    Text(
                      widget.dataInfo.suggestions,
                      style: const TextStyle(
                        fontSize: 14,
                        fontWeight: FontWeight.w400,
                        color: KBlackClr,
                      ),
                      textAlign: TextAlign.justify,
                    ),
                    SizedBox(
                      height: size.height * 0.025,
                    ),
                  ],
                ),
                const Spacer(),
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
                    "Back to Home",
                    style: TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                )
              ],
            ),
          ),
        ),
      ),
    );
  }
}
