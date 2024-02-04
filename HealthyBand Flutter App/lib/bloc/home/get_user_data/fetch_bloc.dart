import 'package:bloc/bloc.dart';
import 'package:healthify/bloc/home/get_user_data/fetch_bloc_event.dart';
import 'package:healthify/bloc/home/get_user_data/fetch_bloc_state.dart';
import 'package:healthify/service/ApiService.dart';

class FetchUserDataBloc
    extends Bloc<FetchUserDataBlocEvent, FetchUserDataBlocState> {
  final ApiService apiService = ApiService();
  FetchUserDataBloc() : super(FetchingDataInitial()) {
    on<GetUserData>((event, emit) async {
      emit(FetchingDataLoading());

      try {
        final res = await apiService.getUserData();
        print("This is Final res");
        print(res);

        emit(FetchingDataSuccess(user: res.user!));
      } catch (err) {
        print("Heres the error");
        emit(FetchingDataFailure(errorMessage: err.toString()));
      }
    });
  }
}
