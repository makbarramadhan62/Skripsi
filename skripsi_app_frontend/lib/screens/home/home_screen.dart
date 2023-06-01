import 'dart:io';

import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:skripsi_app_frontend/screens/home/components/sidebar.dart';
import 'package:skripsi_app_frontend/screens/preview/preview_screen.dart';
import 'package:skripsi_app_frontend/utilities/colors.dart';

import '../how_to_use/how_to_use_screen.dart';
import 'components/button.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  File? image;
  final ImagePicker picker = ImagePicker();

  Future getImageCam() async {
    final pickedFile = await picker.pickImage(source: ImageSource.camera);
    if (pickedFile != null) {
      image = File(pickedFile.path);
    }
    setState(() {});
  }

  Future getImageGallery() async {
    final pickedFile = await picker.pickImage(source: ImageSource.gallery);
    if (pickedFile != null) {
      image = File(pickedFile.path);
    }
    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Scaffold(
      drawer: const SideBar(),
      appBar: AppBar(
        actions: <Widget>[
          IconButton(
            icon: const Icon(
              Icons.question_mark_outlined,
              size: 28,
            ),
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => const HowToUseScreen(),
                ),
              );
            },
          ),
        ],
        iconTheme: const IconThemeData(color: kHighlightTxtClr),
        centerTitle: true,
        title: const Text(
          "Home",
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
          padding: const EdgeInsets.symmetric(
            horizontal: 30,
            vertical: 20,
          ),
          child: Center(
            child: Column(
              children: [
                Column(
                  children: [
                    SizedBox(
                      height: size.height * 0.04,
                    ),
                    Image.asset(
                      "assets/images/gambar_daun+frame.png",
                      width: size.width * 0.8,
                    ),
                    SizedBox(
                      height: size.height * 0.1,
                    ),
                    const Text(
                      "Add an Image to",
                      style: TextStyle(
                        fontSize: 24,
                        fontWeight: FontWeight.w600,
                        color: kBlackClr,
                      ),
                    ),
                    const Text(
                      "Get Started",
                      style: TextStyle(
                        fontSize: 24,
                        fontWeight: FontWeight.w600,
                        color: kHighlightTxtClr,
                      ),
                    ),
                  ],
                ),
                const Spacer(),
                const Text(
                  "Start detecting by adding a picture through the gallery or camera!",
                  style: TextStyle(
                    color: kSubTxtClr,
                    fontSize: 12,
                    fontWeight: FontWeight.w500,
                  ),
                  textAlign: TextAlign.center,
                ),
                SizedBox(
                  height: size.height * 0.02,
                ),
                ElevatedButton(
                  onPressed: () {
                    showGeneralDialog(
                      barrierDismissible: true,
                      barrierLabel: "Select Picture",
                      context: context,
                      pageBuilder: (context, _, __) => Center(
                        child: Container(
                          height: 225,
                          width: 225,
                          margin: const EdgeInsets.symmetric(
                            horizontal: 16,
                          ),
                          padding: const EdgeInsets.symmetric(
                            vertical: 16,
                            horizontal: 24,
                          ),
                          decoration: const BoxDecoration(
                            color: Colors.white,
                            borderRadius: BorderRadius.all(
                              Radius.circular(20),
                            ),
                          ),
                          child: Scaffold(
                            backgroundColor: Colors.transparent,
                            body: Center(
                              child: Column(
                                mainAxisAlignment: MainAxisAlignment.center,
                                children: [
                                  const Text(
                                    "Select Method",
                                    style: TextStyle(
                                      fontSize: 24,
                                      fontWeight: FontWeight.bold,
                                      color: kBlackClr,
                                    ),
                                  ),
                                  const SizedBox(
                                    height: 20,
                                  ),
                                  Button(
                                    press: () async {
                                      await getImageGallery();
                                      if (image != null) {
                                        // ignore: use_build_context_synchronously
                                        Navigator.push(
                                          context,
                                          MaterialPageRoute(
                                            builder: (context) =>
                                                PreviewScreen(image: image),
                                          ),
                                        ).then(
                                          (_) => {
                                            setState(() {
                                              image = null;
                                            })
                                          },
                                        );
                                      }
                                    },
                                    text: "Gallery",
                                  ),
                                  const SizedBox(
                                    height: 15,
                                  ),
                                  Button(
                                    press: () async {
                                      await getImageCam();
                                      if (image != null) {
                                        // ignore: use_build_context_synchronously
                                        Navigator.push(
                                          context,
                                          MaterialPageRoute(
                                            builder: (context) =>
                                                PreviewScreen(image: image),
                                          ),
                                        ).then(
                                          (_) => {
                                            setState(() {
                                              image = null;
                                            })
                                          },
                                        );
                                      }
                                    },
                                    text: "Camera",
                                  )
                                ],
                              ),
                            ),
                          ),
                        ),
                      ),
                    );
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
                    "Add Image",
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

enum DialogsAction { yes, cancel }

class AlertDialogs {
  static Future<DialogsAction> yesCancelDialog(
    BuildContext context,
    String title,
    String body,
  ) async {
    final action = await showDialog(
      context: context,
      barrierDismissible: false,
      builder: (BuildContext context) {
        return AlertDialog(
          shape:
              RoundedRectangleBorder(borderRadius: BorderRadius.circular(10.0)),
          title: Text(
            title,
            style: const TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.w600,
              color: kHighlightTxtClr,
            ),
          ),
          content: Text(
            body,
            style: const TextStyle(
              fontSize: 16,
              fontWeight: FontWeight.w400,
              color: kHighlightTxtClr,
            ),
          ),
          actions: <Widget>[
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                MaterialButton(
                  onPressed: () =>
                      Navigator.of(context).pop(DialogsAction.cancel),
                  child: const Text(
                    'Cancel',
                    style: TextStyle(
                        color: kHighlightTxtClr, fontWeight: FontWeight.bold),
                  ),
                ),
                MaterialButton(
                  onPressed: () => Navigator.of(context).pop(DialogsAction.yes),
                  child: const Text(
                    'Yes',
                    style: TextStyle(
                        color: kDangerClr, fontWeight: FontWeight.w700),
                  ),
                )
              ],
            )
          ],
        );
      },
    );
    return (action != null) ? action : DialogsAction.cancel;
  }
}
