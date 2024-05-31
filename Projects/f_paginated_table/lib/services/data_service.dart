import '../models/data_item.dart';

class ApiService {
  static const String _baseUrl = 'https://your-api.com/data';

  Future<List<DataItem>> fetchData(int page, int pageSize) async {
    // final response =
    //     await http.get(Uri.parse('$_baseUrl?page=$page&pageSize=$pageSize'));

    // if (response.statusCode == 200) {
    if (true) {
      var data = [
        {"id": 1, "name": "Loi"},
        {"id": 2, "name": "Tran"},
      ];
      return List<DataItem>.from(data.map((item) => DataItem.fromJson(item)));
    } else {
      final data = [
        {"id": 1, "name": "Loi"},
        {"id": 2, "name": "Tran"},
      ];
      return List<DataItem>.from(data.map((item) => DataItem.fromJson(item)));
      throw Exception('Failed to load data');
    }
  }
}
