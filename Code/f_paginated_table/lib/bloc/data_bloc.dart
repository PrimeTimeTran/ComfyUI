import 'package:f_paginated_table/services/data_service.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import './data_event.dart';
import './data_state.dart';

class DataBloc extends Bloc<DataEvent, DataState> {
  final ApiService _apiService;
  DataBloc(this._apiService) : super(DataInitialState()) {
    on<DataInitial>((event, emit) => emit(state));
    on<FetchData>((event, emit) async {
      try {
        final data = await _apiService.fetchData(event.page, event.pageSize);
        emit(DataLoadSuccess(
          data: data,
          hasReachedMax: false,
        ));
      } catch (e) {
        throw Exception('Failed to load data');
      }
    });
  }
}
