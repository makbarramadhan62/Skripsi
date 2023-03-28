import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;
import 'package:flutter/material.dart';
import 'package:skripsi_app_frontend/screens/failed/failed_screen.dart';
import 'package:skripsi_app_frontend/screens/result/models/list_data.dart';
import 'package:skripsi_app_frontend/screens/result/result_screen.dart';
import 'package:skripsi_app_frontend/utilities/colors.dart';

class PreviewScreen extends StatefulWidget {
  final File? image;

  const PreviewScreen({
    super.key,
    required this.image,
  });

  @override
  State<PreviewScreen> createState() => _PreviewScreenState();
}

class _PreviewScreenState extends State<PreviewScreen> {
  // int idx = 2;
  // get index => idx - 1;
  int? result;

  Future<void> sendData() async {
    final url = Uri.parse(
        'http://192.168.1.10:5000/klasifikasi'); // ganti dengan URL endpoint API Anda
    final request = http.MultipartRequest('POST', url);
    final imageBytes = await widget.image!.readAsBytes();

    final multipartFile = http.MultipartFile.fromBytes(
      'image',
      imageBytes,
      filename: 'my-image.jpg',
    );
    request.files.add(multipartFile);

    final response = await request.send();
    final jsonResponse = jsonDecode(await response.stream.bytesToString());

    if (response.statusCode == 200) {
      final prediction = jsonResponse['Label'];
      setState(() {
        result = prediction;
      });
    } else {
      setState(() {
        Navigator.pushAndRemoveUntil(
            context,
            MaterialPageRoute(builder: (context) => const FailedScreen()),
            (route) => false);
      });
    }
  }

  late final DataInfo dataInfo;

  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: const Icon(
            Icons.arrow_back,
            color: KButtonClr,
          ),
          onPressed: () {
            Navigator.pop(context);
          },
        ),
        centerTitle: true,
        title: const Text(
          "Preview",
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
          padding: const EdgeInsets.all(20),
          child: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Spacer(),
                Container(
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(10),
                    boxShadow: [
                      BoxShadow(
                        color: KBlackClr.withOpacity(0.5),
                        spreadRadius: 2,
                        blurRadius: 5,
                        offset: const Offset(0, 3),
                      ),
                    ],
                  ),
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(10),
                    child: Image.file(
                      widget.image!,
                    ),
                  ),
                ),
                const Spacer(
                  flex: 3,
                ),
                ElevatedButton(
                  onPressed: () async {
                    await sendData();
                    // ignore: use_build_context_synchronously
                    Navigator.pushAndRemoveUntil(
                        context,
                        MaterialPageRoute(
                          builder: (context) => ResultScreen(
                            dataInfo: data[result!],
                          ),
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
                    "Detect",
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
