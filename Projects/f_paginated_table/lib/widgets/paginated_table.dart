import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import '../bloc/data_bloc.dart';
import '../bloc/data_event.dart';
import '../bloc/data_state.dart';

class PaginatedTable extends StatefulWidget {
  const PaginatedTable({super.key});

  @override
  _PaginatedTableState createState() => _PaginatedTableState();
}

class _PaginatedTableState extends State<PaginatedTable> {
  final _scrollController = ScrollController();
  final _pageSize = 20;
  int _currentPage = 1;

  bool get _isBottom {
    if (!_scrollController.hasClients) return false;
    final maxScroll = _scrollController.position.maxScrollExtent;
    final currentScroll = _scrollController.offset;
    return currentScroll >= (maxScroll * 0.9);
  }

  @override
  Widget build(BuildContext context) {
    return BlocBuilder<DataBloc, DataState>(
      builder: (context, state) {
        if (state is DataInitial) {
          return const Center(child: CircularProgressIndicator());
        } else if (state is DataLoading) {
          return const Center(child: CircularProgressIndicator());
        } else if (state is DataLoadSuccess) {
          _currentPage++;
          return ListView.builder(
            controller: _scrollController,
            itemCount: state.data.length + (state.hasReachedMax ? 0 : 1),
            itemBuilder: (context, index) {
              if (index >= state.data.length) {
                return const Center(child: CircularProgressIndicator());
              }

              final item = state.data[index];
              return ListTile(
                title: Text(item.name),
              );
            },
          );
        } else if (state is DataError) {
          return Container();
        } else {
          return Container();
        }
      },
    );
  }

  @override
  void dispose() {
    _scrollController.dispose();
    super.dispose();
  }

  @override
  void initState() {
    super.initState();
    _scrollController.addListener(_onScroll);
    _fetchData();
  }

  void _fetchData() {
    context
        .read<DataBloc>()
        .add(FetchData(page: _currentPage, pageSize: _pageSize));
  }

  void _onScroll() {
    if (_isBottom) {
      _fetchData();
    }
  }
}
