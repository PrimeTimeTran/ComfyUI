import '../models/data_item.dart';

class DataInitialState extends DataState {}

class DataLoadSuccess extends DataState {
  bool hasReachedMax = false;
  List<DataItem> data = [];
  DataLoadSuccess({required this.data, required this.hasReachedMax});
}

abstract class DataState {}

class DataUpdateState extends DataState {
  bool? initialState;

  DataUpdateState({
    this.initialState,
  });
}
