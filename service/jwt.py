from rest_framework_simplejwt.tokens import RefreshToken


class JWT:
    @staticmethod
    def get_tokens_for_user(user):
        print(user)
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }