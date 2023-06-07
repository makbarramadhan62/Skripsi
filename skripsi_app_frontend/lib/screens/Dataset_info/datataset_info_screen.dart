import 'package:flutter/material.dart';
import 'package:skripsi_app_frontend/screens/Dataset_info/models/dataset_info.dart';
import 'package:skripsi_app_frontend/utilities/colors.dart';

class DatasetScreen extends StatelessWidget {
  const DatasetScreen({super.key});

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
          "Dataset Info",
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
        child: ListView.builder(
          itemCount: dataset.length,
          itemBuilder: (context, index) {
            return Container(
              margin: const EdgeInsets.all(20),
              height: size.height * 0.725,
              width: size.width,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(10),
                color: Colors.white,
                boxShadow: [
                  BoxShadow(
                    color: kButtonClr.withOpacity(0.5),
                    spreadRadius: 1,
                    blurRadius: 5,
                    offset: const Offset(0, 2),
                  ),
                ],
              ),
              child: Padding(
                padding: const EdgeInsets.all(20),
                child: Column(
                  children: [
                    Container(
                      height: size.height * 0.05,
                      width: size.width * 0.4,
                      decoration: BoxDecoration(
                        borderRadius: BorderRadius.circular(10),
                        color: Colors.grey[200],
                        boxShadow: [
                          BoxShadow(
                            color: Colors.grey.withOpacity(0.5),
                            spreadRadius: 2,
                            blurRadius: 5,
                            offset: const Offset(0, 3),
                          ),
                        ],
                      ),
                      child: Center(
                        child: Text(
                          dataset[index].name,
                          style: const TextStyle(
                            fontSize: 16,
                            fontWeight: FontWeight.bold,
                            color: kButtonClr,
                          ),
                        ),
                      ),
                    ),
                    SizedBox(
                      height: size.height * 0.01,
                    ),
                    Image.asset(
                      dataset[index].image,
                      width: size.width * 0.4,
                    ),
                    SizedBox(
                      height: size.height * 0.01,
                    ),
                    Text(
                      dataset[index].description,
                      style: const TextStyle(
                        fontSize: 14,
                        fontWeight: FontWeight.w400,
                      ),
                      textAlign: TextAlign.justify,
                    ),
                    SizedBox(
                      height: size.height * 0.025,
                    ),
                    const Text(
                      "Solusi",
                      style: TextStyle(
                        fontSize: 16,
                        fontWeight: FontWeight.bold,
                        color: kButtonClr,
                      ),
                    ),
                    SizedBox(
                      height: size.height * 0.01,
                    ),
                    Row(
                      children: [
                        const Icon(
                          Icons.panorama_fisheye_outlined,
                          size: 16,
                          color: kButtonClr,
                        ),
                        SizedBox(
                          width: size.width * 0.025,
                        ),
                        Expanded(
                          child: Text(
                            dataset[index].solusi_1,
                            textAlign: TextAlign.justify,
                            style: const TextStyle(
                              fontSize: 14,
                              fontWeight: FontWeight.w400,
                            ),
                          ),
                        ),
                      ],
                    ),
                    Row(
                      children: [
                        const Icon(
                          Icons.panorama_fisheye_outlined,
                          size: 16,
                          color: kButtonClr,
                        ),
                        SizedBox(
                          width: size.width * 0.025,
                        ),
                        Expanded(
                          child: Text(
                            dataset[index].solusi_2,
                            textAlign: TextAlign.justify,
                            style: const TextStyle(
                              fontSize: 14,
                              fontWeight: FontWeight.w400,
                            ),
                          ),
                        ),
                      ],
                    ),
                    Row(
                      children: [
                        const Icon(
                          Icons.panorama_fisheye_outlined,
                          size: 16,
                          color: kButtonClr,
                        ),
                        SizedBox(
                          width: size.width * 0.025,
                        ),
                        Expanded(
                          child: Text(
                            dataset[index].solusi_3,
                            textAlign: TextAlign.justify,
                            style: const TextStyle(
                              fontSize: 14,
                              fontWeight: FontWeight.w400,
                            ),
                          ),
                        ),
                      ],
                    )
                  ],
                ),
              ),
            );
          },
        ),
      ),
    );
  }
}
