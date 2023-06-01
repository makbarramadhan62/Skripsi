import 'dart:io';

import 'package:flutter/material.dart';
import 'package:skripsi_app_frontend/screens/Dataset_info/datataset_info_screen.dart';
import 'package:skripsi_app_frontend/screens/app_version/app_version_screen.dart';
import 'package:skripsi_app_frontend/screens/home/home_screen.dart';
import 'package:skripsi_app_frontend/screens/how_to_use/how_to_use_screen.dart';
import 'package:skripsi_app_frontend/utilities/colors.dart';

class SideBar extends StatefulWidget {
  const SideBar({super.key});

  @override
  State<SideBar> createState() => _SideBarState();
}

class _SideBarState extends State<SideBar> {
  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return SafeArea(
      child: Drawer(
        shape: const RoundedRectangleBorder(
          borderRadius: BorderRadius.only(
              topRight: Radius.circular(20), bottomRight: Radius.circular(20)),
        ),
        child: Padding(
          padding: const EdgeInsets.all(20),
          child: Material(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                SizedBox(height: size.height * 0.025),
                Image.asset(
                  "assets/images/logo_landscape.png",
                  scale: 1.5,
                ),
                SizedBox(height: size.height * 0.025),
                buildMenuItem(
                  text: 'Dataset Info',
                  icon: Icons.dataset_outlined,
                  onClicked: () {
                    Navigator.pop(context);
                    Navigator.of(context).push(
                      MaterialPageRoute(
                        builder: (context) => const DatasetScreen(),
                      ),
                    );
                  },
                ),
                SizedBox(height: size.height * 0.025),
                buildMenuItem(
                  text: 'How to use this app?',
                  icon: Icons.question_mark_outlined,
                  onClicked: () {
                    Navigator.pop(context);
                    Navigator.of(context).push(
                      MaterialPageRoute(
                        builder: (context) => const HowToUseScreen(),
                      ),
                    );
                  },
                ),
                SizedBox(height: size.height * 0.025),
                buildMenuItem(
                  text: 'App Version',
                  icon: Icons.info_outline,
                  onClicked: () {
                    Navigator.pop(context);
                    Navigator.of(context).push(
                      MaterialPageRoute(
                        builder: (context) => const AppVersion(),
                      ),
                    );
                  },
                ),
                const Spacer(),
                const Divider(
                  thickness: 2,
                ),
                buildMenuItem(
                  text: 'Exit',
                  icon: Icons.logout,
                  onClicked: () async {
                    final action = await AlertDialogs.yesCancelDialog(
                        context, 'Exit', 'are you sure?');
                    if (action == DialogsAction.yes) {
                      exit(0);
                    }
                  },
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget buildMenuItem({
    required String text,
    required IconData icon,
    VoidCallback? onClicked,
  }) {
    const hoverColor = Colors.white70;

    return ListTile(
      leading: Icon(icon, color: kHighlightTxtClr),
      title:
          Text(text, style: const TextStyle(fontSize: 16, color: kButtonClr)),
      hoverColor: hoverColor,
      onTap: onClicked,
    );
  }
}
