import 'dart:async';
import 'dart:io';
import 'package:dio/dio.dart';
import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
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
  int? result;
  Timer? _timer;
  bool isLoading = false;
  bool isDetect = false;
  CancelToken? _cancelToken;

  late final DataInfo dataInfo;

  @override
  void initState() {
    super.initState();
    _cancelToken = CancelToken();
    _startTimer();
  }

  void _startTimer() {
    const int timeoutDurationInSeconds = 10;
    _timer = Timer(const Duration(seconds: timeoutDurationInSeconds), () {
      _cancelRequest('Request timed out');
    });
  }

  void _cancelRequest(String reason) {
    _cancelToken?.cancel(reason);
    setState(() {
      isLoading = false;
    });
  }

  @override
  void dispose() {
    _cancelToken?.cancel("Request cancelled");
    _timer?.cancel();
    super.dispose();
  }

  Future<void> sendData() async {
    final now = DateTime.now();
    final formattedTime = DateFormat('yyyy_MM_dd_HH_mm_ss').format(now);
    final filename = 'image_$formattedTime.jpg';
    const int timeoutDurationInSeconds = 10;

    try {
      final dio = Dio();
      dio.options.sendTimeout =
          const Duration(seconds: timeoutDurationInSeconds);
      const url =
          'http://192.168.29.36:5000/klasifikasi'; // Ganti dengan URL endpoint API
      final imageBytes = widget.image!.readAsBytesSync();

      final formData = FormData.fromMap({
        'image': MultipartFile.fromBytes(
          imageBytes,
          filename: filename,
        ),
      });

      final response = await dio.post(
        url,
        data: formData,
        cancelToken: _cancelToken,
      );

      if (response.statusCode == 200) {
        _timer?.cancel();
        final jsonResponse = response.data;
        final prediction = jsonResponse['Label'];
        setState(() {
          result = prediction;
          isLoading = false;
          isDetect = true;
          print(result);
        });
      }
    } catch (error) {
      setState(() {
        isLoading = false;
        isDetect = false;
      });
    }
  }

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
        centerTitle: true,
        title: const Text(
          "Pratinjau",
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
                        color: kBlackClr.withOpacity(0.5),
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
                    setState(() {
                      isLoading = true;
                    });
                    await sendData();
                    isDetect
                        // ignore: use_build_context_synchronously
                        ? Navigator.pushAndRemoveUntil(
                            context,
                            MaterialPageRoute(
                              builder: (context) => ResultScreen(
                                dataInfo: data[result!],
                              ),
                            ),
                            (route) => false,
                          )
                        // ignore: use_build_context_synchronously
                        : Navigator.pushAndRemoveUntil(
                            context,
                            MaterialPageRoute(
                              builder: (context) => const FailedScreen(),
                            ),
                            (route) => false,
                          );
                  },
                  style: ElevatedButton.styleFrom(
                    alignment: Alignment.center,
                    padding: const EdgeInsets.all(5),
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
                  child: isLoading
                      ? const Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            SizedBox(
                              height: 20,
                              width: 20,
                              child: CircularProgressIndicator(
                                strokeWidth: 3,
                                color: Colors.white,
                              ),
                            ),
                            SizedBox(
                              width: 10,
                            ),
                            Text(
                              "Tunggu Sebentar...",
                              style: TextStyle(
                                fontSize: 16,
                                fontWeight: FontWeight.w600,
                              ),
                            )
                          ],
                        )
                      : const Text(
                          "Deteksi",
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
