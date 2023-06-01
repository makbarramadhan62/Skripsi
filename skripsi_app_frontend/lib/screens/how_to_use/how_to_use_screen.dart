import 'package:carousel_slider/carousel_slider.dart';
import 'package:flutter/material.dart';
import 'package:skripsi_app_frontend/utilities/colors.dart';

class HowToUseScreen extends StatefulWidget {
  const HowToUseScreen({super.key});

  @override
  State<HowToUseScreen> createState() => _HowToUseScreenState();
}

class _HowToUseScreenState extends State<HowToUseScreen> {
  int _current = 0;
  final CarouselController _controller = CarouselController();

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    final List<Widget> data = [
      Column(
        children: [
          Image.asset(
            "assets/Mockup/1_WelcomeScreen.png",
            height: size.height * 0.7,
          ),
          SizedBox(
            height: size.height * 0.001,
          ),
          Padding(
            padding: EdgeInsets.symmetric(horizontal: size.width * 0.125),
            child: const Text(
              "Click Get Started to start using the App",
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
                color: kHighlightTxtClr,
              ),
              textAlign: TextAlign.center,
            ),
          )
        ],
      ),
      Column(
        children: [
          Image.asset(
            "assets/Mockup/2_HomeScreen.png",
            height: size.height * 0.7,
          ),
          SizedBox(
            height: size.height * 0.001,
          ),
          Padding(
            padding: EdgeInsets.symmetric(horizontal: size.width * 0.125),
            child: const Text(
              "Click Add Image to Select Method",
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
                color: kHighlightTxtClr,
              ),
              textAlign: TextAlign.center,
            ),
          )
        ],
      ),
      Column(
        children: [
          Image.asset(
            "assets/Mockup/3_HomeScreen_AddImage.png",
            height: size.height * 0.7,
          ),
          SizedBox(
            height: size.height * 0.001,
          ),
          Padding(
            padding: EdgeInsets.symmetric(horizontal: size.width * 0.125),
            child: const Text(
              "Select Method to Add Image",
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
                color: kHighlightTxtClr,
              ),
              textAlign: TextAlign.center,
            ),
          )
        ],
      ),
      Column(
        children: [
          Image.asset(
            "assets/Mockup/4_PreviewScreen.png",
            height: size.height * 0.7,
          ),
          SizedBox(
            height: size.height * 0.001,
          ),
          Padding(
            padding: EdgeInsets.symmetric(horizontal: size.width * 0.125),
            child: const Text(
              "Click Detect to Start Detecting the Image",
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
                color: kHighlightTxtClr,
              ),
              textAlign: TextAlign.center,
            ),
          )
        ],
      ),
      Column(
        children: [
          Image.asset(
            "assets/Mockup/5_ResultScreen.png",
            height: size.height * 0.7,
          ),
          SizedBox(
            height: size.height * 0.001,
          ),
          Padding(
            padding: EdgeInsets.symmetric(horizontal: size.width * 0.125),
            child: const Text(
              "The Result will be Display in the Classification Result",
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
                color: kHighlightTxtClr,
              ),
              textAlign: TextAlign.center,
            ),
          )
        ],
      ),
    ];

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
          "How to Use this App?",
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
          padding: const EdgeInsets.all(10),
          child: Column(children: [
            Expanded(
              child: CarouselSlider(
                items: data,
                carouselController: _controller,
                options: CarouselOptions(
                  viewportFraction: 1,
                  enlargeCenterPage: true,
                  aspectRatio: 9 / 16,
                  onPageChanged: (index, reason) {
                    setState(
                      () {
                        _current = index;
                      },
                    );
                  },
                ),
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: data.asMap().entries.map((entry) {
                return GestureDetector(
                  onTap: () => _controller.animateToPage(entry.key),
                  child: Container(
                    width: size.width * 0.025,
                    height: size.height * 0.01,
                    margin: const EdgeInsets.symmetric(
                        vertical: 8.0, horizontal: 4.0),
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      color: (Theme.of(context).brightness == Brightness.dark
                              ? Colors.white
                              : kHighlightTxtClr)
                          .withOpacity(_current == entry.key ? 0.9 : 0.4),
                    ),
                  ),
                );
              }).toList(),
            ),
          ]),
        ),
      ),
    );
  }
}
