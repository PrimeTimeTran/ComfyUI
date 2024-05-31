// part of 'data_bloc.dart';
class DataError extends DataEvent {}

abstract class DataEvent {}

class DataInitial extends DataEvent {}

class DataLoaded extends DataEvent {
  final List data;

  DataLoaded({required this.data});
}

class DataLoading extends DataEvent {}

class FetchData extends DataEvent {
  final int page;
  final int pageSize;

  FetchData({this.page = 1, this.pageSize = 10});
}
