class DatasetInfo {
  late final double height;
  late final String name, image, description, solusi_1;

  DatasetInfo({
    required this.height,
    required this.name,
    required this.image,
    required this.description,
    required this.solusi_1,
  });
}

List dataset = [
  DatasetInfo(
    height: 450,
    name: "#1 Bercak Daun",
    image: "assets/images/1_bercakDaun.png",
    description:
        "Gejala yang dapat dilihat pada penyakit bercak daun yaitu pada sisi atas daun terdapat bercak-bercak berwarna hijau kekuningan",
    solusi_1:
        "Cara Pengendalian dari penyakit ini ada beberapa cara yaitu dengan memetik dan membakar daun yang terinfeksi dan penyemprotan tanaman dengan menggunakan fungisida (mankozeb, oksiklorida tembaga atau benomyl)",
  ),
  DatasetInfo(
    height: 600,
    name: "#2 Bercak Merah",
    image: "assets/images/2_bercakMerah.png",
    description:
        "Gejala yang dapat dilihat pada penyakit bercak merah yaitu sebagian daun hijau mendadak mati dan berubah warna menjadi coklat dengan jaringan sekitarnya berubah menjadi kuning atau merah. Bagian daun yang kering menyebar dan keseluruhan daun bisa mengkerut dan rontok. Sulur yang terinfeksi kemudian akan mati dalam waktu 2-3 tahun. Varietas yang toleran akan bertahan dalam waktu lebih dari 5 tahun",
    solusi_1:
        "Cara Pengendalian dari penyakit ini yaitu dengan melakukan pengendalian vektor dengan menggunakan jaring atau insektisida, pemusnahan tanaman inang liar dan gulma untuk mengurangi sumber penyakit, perlakuan air panas untuk bahan stek (20 menit pada suhu 50°C atau 180 menit pada suhu 45°C), dan pemangkasan cabang sakit atau keseluruhan tanaman untuk membuang sumber penyakit",
  ),
  DatasetInfo(
    height: 575,
    name: "#3 Embun Tepung Palsu",
    image: "assets/images/4_embunTepungPalsu.png",
    description:
        "Gejala yang dapat dilihat pada penyakit embun tepung palsu yaitu jamur yang menyerang daun, tunas dan buah muda, serangan pada ujung tunas menyebabkan kering dan patah. Serangan pada sisi atas daun ditandai bercak kuning kehijauan yang tidak berbatas tegas, sedangkan serangan pada buah muda menyebabkan busuk abu-abu. Kondisi yang menguntungkan perkembangan patogen adalah suhu rendah, kelembapan tinggi. Hujan merupakan pemicu epidemi",
    solusi_1:
        "Cara Pengendalian dari penyakit ini yaitu mengurangi kelembapan kebun, melakukan sanitasi kebun dengan memangkas tunas dan buah yang terinfeksi, melindungi tanaman dengan fungisida tembaga atau fungisida organik dan melindungi tanaman dengan atap plastik pada musim hujan",
  ),
  DatasetInfo(
    height: 500,
    name: "#4 Hama tungau Merah",
    image: "assets/images/5_hamaTungau.png",
    description:
        "Gejala yang dapat dilihat pada penyakit hama tungau merah yaitu biasanya menyerang daun dengan cara menghisap cairan daun tanaman anggur. Hama ini juga menyebabkan terjadinya bercak-bercak pada daun hingga berubah menjadi hitam. Tanaman anggur yang terkena penyakit ini akan menjadi kerdil dan produktifitasnya menurun",
    solusi_1:
        "Cara Pengendalian dari penyakit ini yaitu dengan melakukan penyemprotan dengan akarisida berbahan aktif abjection (numectin, alfamec, agrimec, demolish atau bamec) dan taburkan Bubur Bordo atau Bubur California pada daun",
  ),
];
