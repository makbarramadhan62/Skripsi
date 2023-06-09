import 'package:flutter/material.dart';
import 'package:skripsi_app_frontend/utilities/colors.dart';

class AppVersion extends StatelessWidget {
  const AppVersion({super.key});

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: const Icon(
            Icons.arrow_back,
            color: kButtonClr,
          ),
          onPressed: () {
            Navigator.pop(context);
          },
        ),
        iconTheme: const IconThemeData(color: kButtonClr),
        centerTitle: true,
        title: const Text(
          "Versi Aplikasi",
          style: TextStyle(
            fontSize: 20,
            fontWeight: FontWeight.bold,
            color: kButtonClr,
          ),
        ),
        backgroundColor: Colors.transparent,
        elevation: 0,
      ),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(20),
          child: Column(
            children: [
              const Spacer(),
              Column(
                children: [
                  Image.asset(
                    'assets/images/logo.png',
                    width: 250,
                    height: 250,
                  ),
                  SizedBox(
                    height: size.height * 0.025,
                  ),
                  const Text(
                    "Versi 1.0 Beta",
                    style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.w500,
                      color: kHighlightTxtClr,
                    ),
                  ),
                ],
              ),
              const Spacer(),
              const Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  Icon(
                    Icons.copyright_outlined,
                    color: kHighlightTxtClr,
                  ),
                  SizedBox(
                    width: 5,
                  ),
                  Text(
                    "marmdhn_",
                    style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.w500,
                      color: kHighlightTxtClr,
                    ),
                  ),
                ],
              )
            ],
          ),
        ),
      ),
    );
  }
}
