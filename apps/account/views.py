from rest_framework import generics, status
from rest_framework.response import Response
from .models import LedgerAccount, SubAccount
from .serializers import LedgerAccountSerializer, SubAccountSerializer

class LedgerAccountCreateListView(generics.ListCreateAPIView):
    queryset = LedgerAccount.objects.all()
    serializer_class = LedgerAccountSerializer

    def post(self, request, *args, **kwargs):
        account_data = request.data
        
        depth = int(account_data.get("depth", 1)) 
        num_sub_accounts = int(account_data.get("num_sub_accounts", 1))
        ledger_account_data = {
            "ledger_name": account_data.get("ledger_name"),
            "account_type": account_data.get("account_type"),
            "type_status": account_data.get("type_status"),
            "sub_accounts": []  # Initialize empty sub_accounts list
        }

        serializer = LedgerAccountSerializer(data=ledger_account_data)
        if serializer.is_valid():
            ledger_account = serializer.save()
            
            root_sub_accounts = self._generate_sub_accounts(num_sub_accounts, depth)
            
            for sub_account_data in root_sub_accounts:
                self._create_sub_account_tree(sub_account_data, None, ledger_account)
            
            # Fetch only the created sub_accounts
            sub_accounts = ledger_account.sub_accounts.all() 
            sub_account_serializer = SubAccountSerializer(sub_accounts, many=True)
            
            return Response(sub_account_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _create_sub_account_tree(self, sub_account_data, parent, ledger_account):
        sub_account = SubAccount.objects.create(
            name=sub_account_data["name"],
            parent=parent,
            ledger_account=ledger_account
        )
            
        children = sub_account_data.get("children", [])
        for child_data in children:
            self._create_sub_account_tree(child_data, sub_account, ledger_account)
            
    def _generate_sub_accounts(self, num_sub_accounts, depth, current_depth=1):
        if current_depth > depth:
            return []
        
        sub_accounts = []
        for i in range(num_sub_accounts):
            sub_account_data = {
                "name": f"SubAccount Level {current_depth} - {i + 1}",
                "children": self._generate_sub_accounts(num_sub_accounts, depth, current_depth + 1)
            }
            sub_accounts.append(sub_account_data)
        
        return sub_accounts
    
class LedgerAccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LedgerAccount.objects.all()
    serializer_class = LedgerAccountSerializer

class SubAccountCreateListView(generics.ListCreateAPIView):
    queryset = SubAccount.objects.all()
    serializer_class = SubAccountSerializer
 
class SubAccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubAccount.objects.all()
    serializer_class = SubAccountSerializer
    
    
    